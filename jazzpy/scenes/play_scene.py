"""
Module with the scene used to represent
levels of the game.
"""
import pygame

from jazzpy import GAME_SETTINGS
from jazzpy.camera.camera import Camera
from jazzpy.models.jazz.jazz import Jazz
from jazzpy.models.misc.hud import Hud
from jazzpy.scenes.abstract_scene import Scene


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
            GAME_SETTINGS["screen_settings"]["screen_width"],
            GAME_SETTINGS["screen_settings"]["screen_height"] - self.hud.HUD_HEIGHT,
            self.level.total_level_width,
            self.level.total_level_height,
        )

        # # bullets
        # self.bullets = pygame.sprite.Group()

        # music
        pygame.mixer.music.load(self.level.level_music_file)
        pygame.mixer.music.play(-1)  # loops forever the music of the level

    def _get_player_events(self):
        """
        Method that gets pygame's events from the queue.

        Args:
            events (list of pygame.event.Event): list of events

        Returns:
            (list): list of pressed keys by the player.
        """
        pressed_states = pygame.key.get_pressed()

        pressed_keys = [
            pressed_states[key]
            for key in (
                # pygame.K_UP,
                # pygame.K_DOWN,
                pygame.K_LEFT,
                pygame.K_RIGHT,
                pygame.K_LALT,
                pygame.K_SPACE,
            )
        ]

        return pressed_keys

    def update(self):
        """
        Method that calls update on every entity/sprite on the scene in order
        to update its contents positions and states.
        """
        pressed_keys = self._get_player_events()

        self.jazz.update(pressed_keys, self.level.platforms)
        self.jazz.bullets.update(self.level.platforms)

    def render_on(self, screen):
        """
        Method that blits things on the main screen (surface) of the game.

        Args:
            screen (pygame.Surface): the main game screen to draw surfaces onto.
        """
        # updates the camera offset based on jazz
        self.camera.compute_offset(self.jazz)

        # platforms blitting
        for platform in self.level.platforms:
            screen.blit(platform.image, self.camera.apply_offset(platform))

        for bullet in self.jazz.bullets.sprites():
            screen.blit(bullet.image, self.camera.apply_offset(bullet))

            if bullet.has_hit:
                screen.blit(bullet.image, self.camera.apply_offset(bullet))
                bullet.kill()

        # bullets are removed due to collision in the group

        # jazz blitting
        screen.blit(self.jazz.image, self.camera.apply_offset(self.jazz))
        screen.blit(
            self.hud.image,
            (
                0,
                GAME_SETTINGS["screen_settings"]["screen_height"] - self.hud.HUD_HEIGHT,
                self.hud.HUD_WIDTH,
                self.hud.HUD_HEIGHT,
            ),
        )
