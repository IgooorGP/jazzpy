"""
Module with the class representation
of Jazz the Jack Rabbit.
"""
import pygame
from sprites.spritesheet import SpriteSheet


class Jazz(pygame.sprite.Sprite):
    """
    Jazz's class.
    """

    SPRITE_SHEET = SpriteSheet("./sprites/jazz/jazz.png")
    DEFAULT_POSITION_SPRITE = (20, 20, 30, 35)

    def __init__(self):
        super(pygame.sprite.Sprite, self).__init__()
        self.jazz_img = self.SPRITE_SHEET.get_image(self.DEFAULT_POSITION_SPRITE)
        self.rect = pygame.Rect(0, 0, 35, 35)

