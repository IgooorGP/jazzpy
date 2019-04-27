"""
Module with the class used to represent
the platforms of th game.
"""
import pygame


class Platform(pygame.sprite.Sprite):
    """
    Class used to represent the platforms of the levels.
    """

    def __init__(self, level_x, level_y, image, is_collidable=True, *groups):
        """
        Creates a new platform at the position x, y of the level
        with the width and height of image from the spritesheet.
        """
        super().__init__(*groups)

        self.image = image
        self.is_collidable = is_collidable
        self.rect = pygame.Rect(level_x, level_y, image.get_width(), image.get_height())
