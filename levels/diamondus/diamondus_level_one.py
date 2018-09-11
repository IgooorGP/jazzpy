"""
Module with the concrete implementation of the 
first level of the Diamondus world.
"""

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

    def __init__(self):
        """
        Default constructor.
        """
        # initializes sprite_sheet and platforms variables
        super(DiamondusLevelOne, self).__init__(
            "./sprites/levels/diamondus/diamondus.png",
            "./levels/diamondus/diamondus_one.txt",
            platforms_width=40,
            platforms_height=40,
        )

    def level_char_code_to_platform(self, level_char_code, level_x, level_y):
        """
        Non-abstract implementation of the method that converts level_char_codes
        into Platform objects at the right positions of the level.
        """
        if level_char_code == "F":
            image = self.sprite_sheet.get_image(self.FILL_SPRITE_1, (self.platforms_width, self.platforms_height))
        if level_char_code == "T":
            image = self.sprite_sheet.get_image(self.TOP_SPRITE_1, (self.platforms_width, self.platforms_height))

        return Platform(level_x, level_y, image)
