"""
Module with general configurations of the game.
"""
import os

DEBUG = True

SCREEN_CAPTION = "JazzPy - Jazz Jackrabbit by Epic MegaGames (1994) Remake"

VIDEO_OPTIONS = {"max_fps": 60, "screen_width": 800, "screen_height": 600}

PROJECT_ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

JAZZ_OBSERVABLE_ID = "jazz"
