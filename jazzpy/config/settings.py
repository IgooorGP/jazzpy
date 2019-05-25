"""
Module used to configure the game. Some options are inserted
when the before_gameinit_hook is executed.
"""
import os

DEBUG = True

SCREEN_CAPTION = "JazzPy - Jazz Jackrabbit by Epic MegaGames (1994) Remake"

VIDEO_OPTIONS = {"max_fps": 60, "screen_width": 800, "screen_height": 600}

PROJECT_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

DEFAULT_SPRITESHEET_LEVELS_CHARCODE_LENGTH = 8

DEFAULT_SPRITESHEET_JAZZ_CHARCODE = "JJJJJJJJ"
DEFAULT_SPRITESHEET_NO_PLATFORM_CHARCODE = "........"

DEFAULT_SPRITESHEET_TILE_DIMENSIONS = {
    "width": 32,
    "height": 32,
    "width_correction": 3,
    "height_correction": 3,
}
