"""
Module with the concrete implementation of the
first level of the Diamondus world.
"""

import pygame

from levels.level import Level
from models.platforms.platforms import Platform


class DiamondusLevelOne(Level):
    """
    Concrete implementation of the abstract class Level
    for the first stage of the game of the Diamondus world.
    """

    # has platforms_width and height
    # has sprite_sheet object
    # has platforms list
    TOP_SPRITE_1 = (32, 193, 32, 32)
    FILL_SPRITE_1 = (64, 416, 32, 32)
    RAMP_SPRITE_1 = (257, 352, 31, 31)
    PRE_RAMP_SPRITE_1 = (193, 353, 31, 31)

    def level_char_code_to_platform(self, level_char_code, level_x, level_y):
        """
        Non-abstract implementation of the method that converts level_char_codes
        into Platform objects at the right positions of the level.
        """
        image = None
        platform_dimensions = (self.platforms_width, self.platforms_height)

        if level_char_code == "F":
            image = self.sprite_sheet.get_image(self.FILL_SPRITE_1, dimensions=platform_dimensions)
        elif level_char_code == "T":
            image = self.sprite_sheet.get_image(self.TOP_SPRITE_1, dimensions=platform_dimensions)
        elif level_char_code == " ":
            return None
        elif level_char_code == "\\":
            image = self.sprite_sheet.get_image(self.RAMP_SPRITE_1, dimensions=platform_dimensions)
        elif level_char_code == "R":
            image = self.sprite_sheet.get_image(self.PRE_RAMP_SPRITE_1, dimensions=platform_dimensions)
        elif level_char_code == "J":
            self.jazz_initial_x, self.jazz_initial_y = level_x, level_y
        else:
            image = self.sprite_sheet.get_image(self.FILL_SPRITE_1, dimensions=platform_dimensions)

        if image:
            return Platform(level_x, level_y, image)
