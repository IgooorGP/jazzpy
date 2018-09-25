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
    STANDARD_GRASS_TOP_SPRITE = (32, 193, 32, 32)  # T1

    # fill sprites
    STANDARD_FILL_SPRITE = (64, 416, 32, 32)  # F1
    SMALL_DIAMONDS_FILL_SPRITE = (96, 193, 32, 32)  # F2
    RED_DIAMOND_FILL_SPRITE = (63, 225, 26, 29)  # F3
    TEAL_DIAMOND_FILL_SPRITE = (38, 226, 26, 29)  # F4
    GREEN_DIAMOND_FILL_SPRITE = (2, 226, 26, 29)  # F5
    PRE_RAMP_FILL_SPRITE = (193, 353, 31, 31)  # F6
    DIAMONDS_FULL_FILL_SPRITE = (167, 293, 51, 51)  # F7
    UP_TRIANGLE_RIGHT_FILL = (99, 286, 28, 30)  # F8
    UP_TRIANGLE_LEFT_FILL = (4, 320, 28, 28)  # F9

    RAMP_GRASS_SPRITE_1 = (257, 352, 31, 31)  # R1
    UP_GRASS_SPRITE_1 = (96, 352, 32, 30)  # U1

    EDGE_GRASS_SPRITE_LEFT_1 = (164, 191, 28, 32)  # E1
    EDGE_GRASS_SPRITE_RIGHT_1 = (219, 192, 28, 32)  # E2

    def level_char_code_to_platform(self, level_char_code, level_x, level_y):
        """
        Non-abstract implementation of the method that converts level_char_codes
        into Platform objects at the right positions of the level.
        """
        image = None
        platform_dimensions = (self.platforms_width, self.platforms_height)

        if level_char_code == "F1":
            image = self.sprite_sheet.get_image(self.STANDARD_FILL_SPRITE, dimensions=platform_dimensions)
        elif level_char_code == "T1":
            image = self.sprite_sheet.get_image(self.STANDARD_GRASS_TOP_SPRITE, dimensions=platform_dimensions)
        elif level_char_code == "  ":
            return None
        elif level_char_code == "R1":
            image = self.sprite_sheet.get_image(self.RAMP_GRASS_SPRITE_1, dimensions=platform_dimensions)
        elif level_char_code == "F9":
            image = self.sprite_sheet.get_image(self.PRE_RAMP_FILL_SPRITE, dimensions=platform_dimensions)
        elif level_char_code == "JJ":
            self.jazz_initial_x, self.jazz_initial_y = level_x, level_y
        elif level_char_code == "F2":
            image = self.sprite_sheet.get_image(self.SMALL_DIAMONDS_FILL_SPRITE, dimensions=platform_dimensions)
        elif level_char_code == "F6":
            image = self.sprite_sheet.get_image(self.PRE_RAMP_FILL_SPRITE, dimensions=platform_dimensions)
        else:
            image = self.sprite_sheet.get_image(self.STANDARD_FILL_SPRITE, dimensions=platform_dimensions)

        if image:
            return Platform(level_x, level_y, image)
