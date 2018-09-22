"""
Module with the scene used to represent
levels of the game.
"""
import pygame

from camera.camera import Camera
from config import SCREEN_HEIGHT, SCREEN_WIDTH
from models.jazz.jazz import Jazz
from scenes.abstract_scene import Scene
from models.misc.bullet import Bullet
from models.misc.hud import Hud


class PlayScene(Scene):
    """
    Scene class implementation for play scenes
    of the game.
    """

    def __init__(self, level):
        """ 
        Default constructor of the playscene. Builds a level, creates
        a Jazzi instance and starts the play scene camera.

        Args:
            level (Level): a reference of a level implementation.
        """
        super(PlayScene, self).__init__()
        self.level = level

        # builds the level
        self.level.build()

        # gets jazz
        self.jazz = Jazz(level.jazz_initial_x, level.jazz_initial_y)

        # game HUD
        self.hud = Hud()

        # starts the camera
        self.camera = Camera(
            SCREEN_WIDTH,
            SCREEN_HEIGHT - self.hud.HUD_HEIGHT,
            self.level.total_level_width,
            self.level.total_level_height,
        )

        # bullets
        self.bullets = pygame.sprite.Group()
        self.oldtime = 0

        # music
        pygame.mixer.music.load(self.level.level_music_file)
        pygame.mixer.music.play(-1)  # loops forever the music of the level

    def handle_events(self, events):
        """
        Method that handles player's events.

        Args:
            events (list of pygame.event.Event): list of events
        """
        pass

    def update(self):
        """
        Method that calls update on every entity/sprite on the scene in order
        to update its contents positions and states.
        """
        # gets a bool state list of events
        pressed_states = pygame.key.get_pressed()

        # gets bool state of specific keys that matters
        pressed_keys = [
            pressed_states[key]
            for key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LALT, pygame.K_SPACE)
        ]

        # unpacks states
        up, down, left, right, alt, space = pressed_keys

        # updates jazz
        self.jazz.update(up, down, left, right, alt, space, self.level.platforms)
        self.bullets.update(self.level.platforms)

        if space:

            newtime = pygame.time.get_ticks()

            if self.oldtime == 0 or newtime - self.oldtime > self.jazz.INITIAL_SHOOTING_DELAY:

                if newtime - self.oldtime < 1000:
                    if self.jazz.direction == "right":
                        bullet = Bullet(self.jazz.rect.midright[0], self.jazz.rect.midright[1] + 5, self.jazz.direction)
                    else:
                        bullet = Bullet(self.jazz.rect.midleft[0], self.jazz.rect.midleft[1] + 5, self.jazz.direction)

                    self.bullets.add(bullet)

                self.oldtime = pygame.time.get_ticks()

        # updates the camera state
        self.camera.update(self.jazz)

    def render_on(self, screen):
        """
        Method that blits things on the main screen (surface) of the game.

        Args:
            screen (pygame.Surface): the main game screen to draw surfaces onto.
        """
        # platforms blitting
        for platform in self.level.platforms:
            screen.blit(platform.image, self.camera.apply(platform))

        for bullet in self.bullets.sprites():
            screen.blit(bullet.image, self.camera.apply(bullet))

            if bullet.has_hit:
                screen.blit(bullet.image, self.camera.apply(bullet))
                bullet.kill()

        # bullets are removed due to collision in the group

        # jazz blitting
        screen.blit(self.jazz.image, self.camera.apply(self.jazz))
        screen.blit(self.hud.image, (0, SCREEN_HEIGHT - self.hud.HUD_HEIGHT, self.hud.HUD_WIDTH, self.hud.HUD_HEIGHT))
