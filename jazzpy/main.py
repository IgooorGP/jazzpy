"""
Main game module.
"""
import pygame
from jazzpy.config.settings import SCREEN_CAPTION
from jazzpy.config.settings import VIDEO_OPTIONS
from jazzpy.scenes.manager import SceneManager


class JazzPy:
    """
    Main game class.
    """

    def __init__(self):
        """
        Initializes pygame, the game clock, the game running state
        and the screen/scene manager.
        """
        # intializes Pygame
        pygame.init()
        pygame.mixer.init()  # iniits mixer module for sound

        self.screen = self._load_screen(SCREEN_CAPTION)
        self.scene_manager = SceneManager()
        self.clock = pygame.time.Clock()
        self.is_gameover = False

    @classmethod
    def _load_screen(cls, screen_caption):
        """
        Initializes the game screen.
        """
        screen = pygame.display.set_mode(
            (VIDEO_OPTIONS["screen_width"], VIDEO_OPTIONS["screen_height"]), pygame.FULLSCREEN
        )

        # caption setting
        pygame.display.set_caption(screen_caption)

        return screen

    def _before_gameover_hook(self):
        """
        Executes some final code before finally closing the game.
        """
        self.is_gameover = True

        pygame.quit()

    def _check_for_gameover(self) -> None:
        """
        Reads Pygame's events to see if the player wants to quit or if
        the game is over. Executes the gameover hook before closing.
        """
        if pygame.event.get(pygame.QUIT):
            self._before_gameover_hook()

        if self.scene_manager.current_scene_captured_quit_event():
            self._before_gameover_hook()

    def _wait_for_next_frame(self):
        """
        Uses Pygame's Clock to set a time delay before the next frame
        gets updated.

        Sleeps based on seconds per frame to proceed with next instructions
        """
        self.clock.tick(VIDEO_OPTIONS["max_fps"])

        # print("FPS: {fps}".format(fps=self.clock.get_fps()))

    def _update_state(self):
        """
        Updates game state for each frame.
        """
        # clears screen before next update
        self.screen.fill((0, 0, 0))

        # updates the scene based on user event
        self.scene_manager.update_current_scene()

        # updates the whole display
        pygame.display.flip()

    def play(self):
        """
        Public method that starts the main game/event loop.
        """
        while not self.is_gameover:

            # clock tick before next frame (fixed fps)
            self._wait_for_next_frame()

            # updates game state/screen by getting all events from the queue
            self._update_state()

            # attempts to get the quit event from the event queue
            self._check_for_gameover()
