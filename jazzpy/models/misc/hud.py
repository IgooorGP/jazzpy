"""
Module with the class representation
of Jazz's bullets.
"""
import pygame

from jazzpy.config import GAME_ROOT
from jazzpy.config import SCREEN_HEIGHT
from jazzpy.config import SCREEN_WIDTH
from jazzpy.sprites.spritesheet import SpriteSheet


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
        self.sprite_sheet = SpriteSheet(GAME_ROOT + "/sprites/misc/misc.png")
        self.image = self.sprite_sheet.get_image(
            self.HUD_SPRITE, dimensions=(SCREEN_WIDTH, self.HUD_HEIGHT)
        )

    def update(self):
        pass
