"""
Module with a convenience class to get
images from a spritesheet.
"""
import pygame


class SpriteSheet:
    """
    Class that handles getting images from a spritesheet.
    """

    def __init__(self, file_name):
        """
        Default constructor.

        Args:
            file_name(str): relative os.path based on jazz.py file.
        """
        # playing jazz = https://classicreload.com/jazz-jackrabbit.html
        # removing background spritesheet = https://www141.lunapic.com/editor/
        # get spritesheet positions = http://getspritexy.com/

        # background to transparent
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def get_image(self, at):
        """
        Returns a pygame.Surface object with a blit image from
        a spritesheet.

        Args:
            at (tuple): tuple with the following data: x, y, width, height (ints)

        Returns:
            (pygame.Surface): Blited surface (image).
        """
        x, y, width, height = at
        # x = at[0]
        # y = at[1]
        # width = at[2]
        # height = at[3]

        # uses a transparent surface as the base image (pass pygame.SRCALPHA).
        image = pygame.Surface([width, height], pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image
