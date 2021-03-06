"""
Module with the scene used to represent
levels of the game.
"""
from typing import List

import pygame
from jazzpy.scenes.abstract_scene import Scene
from jazzpy.settings.general import VIDEO_OPTIONS
from jazzpy.settings.hud import HUD_HEIGHT
from jazzpy.settings.scenes import BLITTING_X_EXTENSION
from jazzpy.settings.scenes import BLITTING_Y_EXTENSION
from jazzpy.sprites.jazz.jazz import Jazz
from jazzpy.sprites.misc.hud import Hud
from jazzpy.support.camera import Camera


class PlayScene(Scene):
    """
    Scene class implementation for play scenes of the game.
    """

    def __init__(self, level):
        """
        Default constructor of the playscene. Builds a level, creates
        a Jazz instance and starts the play scene camera.

        Args:
            level (Level): a reference of a level implementation.
        """
        super(PlayScene, self).__init__()

        # builds the level
        self.level = level
        self.level.build()

        # game HUD
        self.hud = Hud()

        # gets jazz
        self.jazz = Jazz(level.jazz_initial_x, level.jazz_initial_y, self.hud)

        # starts the camera
        self.camera = Camera(
            VIDEO_OPTIONS["screen_width"],
            VIDEO_OPTIONS["screen_height"] - HUD_HEIGHT,
            self.level.total_level_width,
            self.level.total_level_height,
        )

        self.has_captured_quit_event = False

        # music
        pygame.mixer.music.load(self.level.level_music_file)
        pygame.mixer.music.play(-1)  # loops forever the music of the level

    def _get_pressed_keys(self):
        """
        Method that gets the pressed key events.

        Returns:
            (list): list of pressed keys by the player.
        """
        pressed_states = pygame.key.get_pressed()

        # desired pressed key states for this scene
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

    def _filter_sprites_out_of_screen(self, sprites_list, x_extension=0, y_extension=0):
        """
        Gets all sprites that are on the screen only in order to avoid
        unnecessary collision calculation.
        """
        closest_x = self.jazz.rect.left - int(self.camera.screen_width / 2) - x_extension
        farthest_x = self.jazz.rect.right + int(self.camera.screen_width / 2) + x_extension

        closest_y = self.jazz.rect.top - int(self.camera.screen_height / 2) - y_extension
        farthest_y = self.jazz.rect.bottom + int(self.camera.screen_height / 2) + y_extension

        # zero correction
        if closest_x < 0:
            closest_x = 0

        if closest_y < 0:
            closest_y = 0

        screen_sprites = []

        for sprite in sprites_list:

            within_x = closest_x <= sprite.rect.x <= farthest_x
            within_y = closest_y <= sprite.rect.y <= farthest_y

            if within_x and within_y:
                screen_sprites.append(sprite)

        return screen_sprites

    def update(self):
        """
        Method that calls update on every entity/sprite on the scene in order
        to update its contents positions and states.
        """
        # TODO: handle ESC to show menu and not QUIT the game
        events: List[pygame.event.EventType] = self._get_all_events()

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:

                self.has_captured_quit_event = True
                return

        pressed_keys = self._get_pressed_keys()
        screen_platforms = self._filter_sprites_out_of_screen(self.level.platforms)

        self.jazz.update(pressed_keys, screen_platforms)
        self.jazz.bullets.update(screen_platforms)

    def render(self):
        """
        Method that blits things on the main screen (surface) of the game.

        Args:
            screen (pygame.Surface): the main game screen to draw surfaces onto.
        """
        screen = pygame.display.get_surface()

        # updates the camera offset based on jazz
        self.camera.compute_offset(self.jazz)

        screen_platforms = self._filter_sprites_out_of_screen(
            self.level.platforms, BLITTING_X_EXTENSION, BLITTING_Y_EXTENSION
        )
        screen_bullets = self._filter_sprites_out_of_screen(
            self.jazz.bullets.sprites(), BLITTING_X_EXTENSION, BLITTING_Y_EXTENSION
        )

        # attempt grey filter on platforms
        for platform in screen_platforms:
            screen.blit(platform.image, self.camera.apply_offset(platform))

        for bullet in screen_bullets:
            screen.blit(bullet.image, self.camera.apply_offset(bullet))

            if bullet.has_hit:
                screen.blit(bullet.image, self.camera.apply_offset(bullet))
                bullet.kill()  # bullets are removed due to collision in the group

        # jazz blitting
        screen.blit(self.jazz.image, self.camera.apply_offset(self.jazz))
        screen.blit(self.hud.image, dest=(0, VIDEO_OPTIONS["screen_height"] - HUD_HEIGHT))
