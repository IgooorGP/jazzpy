"""
Module with the class representation
of Jazz's bullets.
"""
import pygame
from sprites.spritesheet import SpriteSheet
from config import SCREEN_WIDTH, SCREEN_HEIGHT


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
        self.sprite_sheet = SpriteSheet("./sprites/misc/misc.png")
        self.image = self.sprite_sheet.get_image(self.HUD_SPRITE, dimensions=(SCREEN_WIDTH, self.HUD_HEIGHT))

    def update(self):
        pass
