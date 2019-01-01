"""
Main game module.
"""
import pygame

from jazzpy import GAME_SETTINGS
from jazzpy.scenes.manager import SceneManager


class JazzPy:
    """
    Main game class.
    """

    SCREEN_CAPTION = "JazzPy - Jazz Jackrabbit by Epic MegaGames (1994) Remake"

    def __init__(self):
        # intializes Pygame
        pygame.init()
        pygame.mixer.init()  # iniits mixer module for sound

        self.screen = self._load_screen(self.SCREEN_CAPTION)
        self.scene_manager = SceneManager()
        self.clock = pygame.time.Clock()
        self.is_game_running = True

    def _load_screen(self, screen_caption):
        """
        Initializes the game screen.
        """
        # screen creation
        screen = pygame.display.set_mode(
            (
                GAME_SETTINGS["screen_settings"]["screen_width"],
                GAME_SETTINGS["screen_settings"]["screen_height"],
            )
        )

        # caption setting
        pygame.display.set_caption(screen_caption)

        return screen

    def _wait_for_next_frame(self):
        """
        Uses Pygame's Clock to set a time delay before the next frame
        gets updated.

        Sleeps based on seconds per frame to proceed with next instructions
        """
        self.clock.tick(GAME_SETTINGS["game_settings"]["max_fps"])

    def _update_state(self, screen):
        """
        Updates game state for each frame.
        """
        # clears screen before next update
        self.screen.fill((0, 0, 0))

        # updates the scene based on user event
        self.scene_manager.update_current_scene(screen)

        # updates the whole display
        pygame.display.flip()

    def play(self):
        """
        Public method that starts the main game/event loop.
        """
        while True:

            # attempts to get the quit event from the event queue
            if pygame.event.get(pygame.QUIT):
                break

            # clock tick before next frame (fixed fps)
            self._wait_for_next_frame()

            # updates game state/screen by getting all events from the queue
            self._update_state(self.screen)
