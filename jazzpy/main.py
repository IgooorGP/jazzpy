"""
Main game module.
"""
import os

import pygame
from jazzpy.config.settings import DEBUG
from jazzpy.config.settings import PROJECT_ROOT_DIR
from jazzpy.config.settings import SCREEN_CAPTION
from jazzpy.config.settings import VIDEO_OPTIONS
from jazzpy.levels.diamondus.diamondus_level_one import DiamondusLevelOne
from jazzpy.scenes.manager import SceneManager
from jazzpy.scenes.play_scene import PlayScene


class JazzPy:
    """
    Main game class.
    """

    def __init__(self):
        """
        Initializes pygame, the game clock, the game running state
        and the screen/scene manager.
        """
        # intializes Pygame modules and the mixer module for sound
        pygame.init()
        pygame.mixer.init()

        # initializes complex objects such as the screen and scene manager
        self.screen = self._load_screen()
        self.scene_manager = self._load_scene_manager()

        self.clock = pygame.time.Clock()
        self.is_gameover = False

    @classmethod
    def _load_screen(cls) -> pygame.Surface:
        """
        Initializes the game screen.
        """
        screen_flags = pygame.FULLSCREEN

        if DEBUG:
            screen_flags = 0

        screen = pygame.display.set_mode(
            (VIDEO_OPTIONS["screen_width"], VIDEO_OPTIONS["screen_height"]), screen_flags
        )

        # caption setting
        pygame.display.set_caption(SCREEN_CAPTION)

        return screen

    @classmethod
    def _load_scene_manager(cls) -> SceneManager:
        """
        Loads the scene manager with the first scene of the game which could be a menu scene or a play scene.
        """
        level_spritesheet_file = os.path.join(
            PROJECT_ROOT_DIR, "jazzpy/spritesheets/levels/diamondus/diamondus.png"
        )
        level_platforms_file = os.path.join(
            PROJECT_ROOT_DIR, "jazzpy/levels/diamondus/diamondus_level_one.txt"
        )
        level_music_file = os.path.join(
            PROJECT_ROOT_DIR, "jazzpy/music/levels/diamondus/diamondus.mp3"
        )

        diamondus_level_one = DiamondusLevelOne(
            spritesheet_file=level_spritesheet_file,
            spritesheet_matrix_dimensions=(22, 9),
            level_platforms_file=level_platforms_file,
            level_music_file=level_music_file,
            platforms_width=60,
            platforms_height=60,
        )

        diamondus_one_scene = PlayScene(diamondus_level_one)

        # Creates the scene manager and loads the first game level: Diamomndus
        scene_manager = SceneManager(initial_scene=diamondus_one_scene)

        return scene_manager

    def _before_gameover_hook(self) -> None:
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

    def _wait_for_next_frame(self) -> None:
        """
        Uses Pygame's Clock to set a time delay before the next frame
        gets updated.

        Sleeps based on seconds per frame to proceed with next instructions
        """
        self.clock.tick(VIDEO_OPTIONS["max_fps"])

        # print("FPS: {fps}".format(fps=self.clock.get_fps()))

    def _update_state(self) -> None:
        """
        Updates game state for each frame.
        """
        # clears screen before next update
        self.screen.fill((0, 64, 255))

        # updates the scene based on user event
        self.scene_manager.update_current_scene()

        # updates the whole display
        pygame.display.flip()

    def play(self) -> None:
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
