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

    def __init__(self, spritesheet_file, level_file, level_music_file, platforms_width, platforms_height):
        """
        Base constructor of a level with empty platforms
        and a spritsheet based on a path to the file.
        """
        self.sprite_sheet = SpriteSheet(spritesheet_file)
        self.level_file = level_file
        self.level_music_file = level_music_file
        self.platforms_width = platforms_width
        self.platforms_height = platforms_height
        self.jazz_initial_x = -1
        self.jazz_initial_y = -1

        # filled after parse_level invocation
        self.total_level_width = 0
        self.total_level_height = 0
        self.platforms = []

    def build(self):
        """
        Parses level files to convert level_char_codes into
        platform objects (pygame.Sprites).
        """
        with open(self.level_file) as fileobj:
            level_x = 0
            level_y = 0

            for line in fileobj:
                # removes whitespaces except spaces
                line = line.strip("\r\n\t")

                for level_char_code in line:

                    image = self.level_char_code_to_platform(level_char_code, level_x, level_y)

                    if image is not None:
                        self.platforms.append(image)

                    level_x += self.platforms_width

                # gets total level width
                self.total_level_width = level_x

                # resets for next row
                level_x = 0
                level_y += self.platforms_height

            # gets total level height
            self.total_level_height = level_y

        if self.jazz_initial_x == -1 or self.jazz_initial_y == -1:
            raise RuntimeError("Unable to find jazz's initial position on the level. Check the map file.")

    @abstractmethod
    def level_char_code_to_platform(self, level_char_code, level_x, level_y):
        """
        Abstract method for Mapping from level character to an actual pygame.Sprite object
        """
        pass
