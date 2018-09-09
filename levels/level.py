"""
Module with the level loader class.
"""
from abc import ABC, abstractmethod
from sprites.spritesheet import SpriteSheet


class Level(ABC):
    """
    Class with methods to parse and load
    levels from txt files.
    """

    def __init__(self, spritesheet_file, level_file):
        """
        Base constructor of a level with empty platforms
        and a spritsheet based on a path to the file.
        """
        self.sprite_sheet = SpriteSheet(spritesheet_file)
        self.level_file = level_file
        self.platforms = []

        # fills platforms of the levels
        self.parse_level()

    def parse_level(self):
        """
        Parses level files to convert level_char_codes into
        platform objects (pygame.Sprites).
        """
        with open(self.level_file) as fileobj:
            for line in fileobj:
                for level_char_code in line:
                    self.platforms.append(self.level_char_code_to_platform(level_char_code))

    @abstractmethod
    def level_char_code_to_platform(self, level_char_code):
        """
        Abstract method for Mapping from level character to an actual pygame.Sprite object
        """
        pass
