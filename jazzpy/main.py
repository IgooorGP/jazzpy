"""
Main game module.
"""
import pygame

from jazzpy.scenes.manager import SceneManager
from jazzpy.settings import game_options


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

    def _get_screen_resolution(self):
        """
        Attempts to get the best screen resolution based on the player's
        screen ratio.
        """
        screen_info = pygame.display.Info()
        aspect_ratio = screen_info.current_w / screen_info.current_h

        # 4 : 3 screens
        if aspect_ratio <= 1.4:
            screen_width, screen_height = 800, 600

        # 4 : 3 to 16:10 (mac)
        elif 1.4 < aspect_ratio <= 1.7:
            screen_width, screen_height = 800, 500

        # 16:9 widescreens
        else:
            screen_width, screen_height = 860, 480

        return screen_width, screen_height

    def _load_screen(self, screen_caption):
        """
        Initializes the game screen.
        """
        screen_width, screen_height = self._get_screen_resolution()
        # print(pygame.display.list_modes())

        # sets game screen settings
        game_options["video_settings"]["screen_width"] = screen_width
        game_options["video_settings"]["screen_height"] = screen_height

        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

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
        self.clock.tick(game_options["video_settings"]["max_fps"])

        # print("FPS: {fps}".format(fps=self.clock.get_fps()))

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
