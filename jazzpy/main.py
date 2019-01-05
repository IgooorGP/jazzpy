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
        """
        Initializes pygame, the game clock, the game running state
        and the screen/scene manager.
        """
        # intializes Pygame
        pygame.init()
        pygame.mixer.init()  # iniits mixer module for sound

        self.screen = self._load_screen(self.SCREEN_CAPTION)
        self.scene_manager = SceneManager()
        self.clock = pygame.time.Clock()
        self.is_gameover = False

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

    def _before_gameover_hook(self):
        """
        Executes some final code before finally closing the game.
        """
        self.is_gameover = True

        pygame.quit()

    def _check_for_gameover(self):
        """
        Reads Pygame's events to see if the player wants to quit or if
        the game is over. Executes the gameover hook before closing.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._before_gameover_hook()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._before_gameover_hook()

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
        while not self.is_gameover:

            # clock tick before next frame (fixed fps)
            self._wait_for_next_frame()

            # updates game state/screen by getting all events from the queue
            self._update_state(self.screen)

            # attempts to get the quit event from the event queue
            self._check_for_gameover()


if __name__ == "__main__":
    game = JazzPy()
    game.play()  # starts the game loop
