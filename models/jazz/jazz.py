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

    DEFAULT_POSITION_SPRITE = (20, 20, 30, 35)

    def __init__(self):
        """
        Default constructor for the Jazz JackRabbit character class.
        """
        # super class init
        super().__init__()

        # loads the sprite_sheet
        self.sprite_sheet = SpriteSheet("./sprites/jazz/jazz.png")

        # jazz imgs
        self.image = self.sprite_sheet.get_image(self.DEFAULT_POSITION_SPRITE)
        self.rect = self.image.get_rect()

    def update(self):
        """
        Updates the current position. Checks for collisions. Listen to events.
        """
        raise NotImplementedError
        # TODO listen to the events, update sprite, etc.

        # if event.type == KEYDOWN:
        #     if event.key == K_d:
        #         move_right = True

        # if event.type == KEYDOWN:
        #     if event.key == K_a:
        #         move_left = True

        # if event.type == KEYUP:
        #     if event.key == K_d:
        #         move_right = False

        # if event.type == KEYUP:
        #     if event.key == K_a:
        #         move_left = False

