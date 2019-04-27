"""
Module used to configure the game. Some options are inserted
when the before_gameinit_hook is executed.
"""
import os

DEBUG = True

SCREEN_CAPTION = "JazzPy - Jazz Jackrabbit by Epic MegaGames (1994) Remake"

VIDEO_OPTIONS = {"max_fps": 60, "screen_width": 800, "screen_height": 600}

GAME_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
