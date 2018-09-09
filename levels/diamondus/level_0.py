"""
Module with the concrete implementation of the 
level 0 of the game: Diamondus world.
"""
from levels.level import Level


class LevelZero(Level):
    """
    Concrete implementation of the abstract class Level
    for the first stage of the game in the Diamondus world.
    """

    def __init__(self):
        """
        Default constructor.
        """
        # initializes sprite_sheet and platforms variables
        super(LevelZero, self).__init__("./sprites/levels/diamondus/diamondus.png", "./levels/diamondus/level_0.txt")

    def level_char_code_to_platform(self, level_char_code):
        """
        Maps level_char_codes into platforms (pygame.Sprites).
        """
        pass
