"""
Module with the class representation
of Jazz's bullets.
"""
import pygame

from jazzpy import GAME_SETTINGS
from jazzpy.spritesheets.spritesheet import SpriteSheet


class Hud(pygame.sprite.Sprite):
    """
    Bullet class.
    """

    HUD_WIDTH = 100
    HUD_HEIGHT = 100
    HUD_SPRITE = (26, 1051, 319, 32)

    def __init__(self):
        """
        Default constructor for the bullets.
        """
        super().__init__()

        # default position
        self.sprite_sheet = SpriteSheet(
            GAME_SETTINGS["folder_settings"]["game_root"] + "spritesheets/misc/misc.png"
        )
        self.image = self.sprite_sheet.get_image(
            self.HUD_SPRITE,
            dimensions=(GAME_SETTINGS["screen_settings"]["screen_width"], self.HUD_HEIGHT),
        )

    def update(self):
        pass