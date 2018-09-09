"""
Module with the concrete implementation of the 
first level of the Diamondus world.
"""
from levels.level import Level
from models.platforms.platforms import Platform


class DiamondusOne(Level):
    """
    Concrete implementation of the abstract class Level
    for the first stage of the game of the Diamondus world.
    """

    TOP_SPRITE_1 = (32, 193, 32, 32)
    FILL_SPRITE_1 = (64, 416, 32, 32)

    def __init__(self):
        """
        Default constructor.
        """
        # initializes sprite_sheet and platforms variables
        super(DiamondusOne, self).__init__(
            "./sprites/levels/diamondus/diamondus.png", "./levels/diamondus/diamondus_one.txt"
        )

    def level_char_code_to_platform(self, level_char_code):
        """
        Maps level_char_codes into platforms (pygame.Sprites).
        """
        # parses every char code in order to create the platforms
        # instantiates a platform object at x, y coords
        # with width a height
        Platform(x, y)

