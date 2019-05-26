"""
Module with the level loader class.
"""
from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Optional
from typing import Tuple

from jazzpy.exceptions.levels import CorruptedLevelFile
from jazzpy.exceptions.levels import MissingJazzInitialPositionOnLevelfile
from jazzpy.settings.levels import DEFAULT_SPRITESHEET_JAZZ_CHARCODE
from jazzpy.settings.levels import DEFAULT_SPRITESHEET_LEVELS_CHARCODE_LENGTH
from jazzpy.settings.levels import DEFAULT_SPRITESHEET_NO_PLATFORM_CHARCODE
from jazzpy.sprites.platforms.platforms import Platform
from jazzpy.support.spritesheet import SpriteSheet


class Level(ABC):
    """
    Class with methods to parse and load
    levels from txt files.
    """

    def __init__(
        self,
        spritesheet_file: str,
        level_platforms_file: str,
        level_music_file: str,
        platforms_width: int,
        platforms_height: int,
        spritesheet_matrix_dimensions: Tuple[int, int] = None,
    ):
        """
        Base constructor of a level with empty platforms
        and a spritsheet based on a path to the file.
        """
        self.sprite_sheet = SpriteSheet(
            spritesheet_file, spritesheet_matrix_dimensions=spritesheet_matrix_dimensions
        )
        self.level_platforms_file = level_platforms_file
        self.level_music_file = level_music_file
        self.platforms_width = platforms_width
        self.platforms_height = platforms_height
        self.jazz_initial_x = -1
        self.jazz_initial_y = -1
        self.jazz_level_char_code = DEFAULT_SPRITESHEET_JAZZ_CHARCODE
        self.no_platform_level_char_code = DEFAULT_SPRITESHEET_NO_PLATFORM_CHARCODE

        # filled after parse_level invocation
        self.total_level_width = 0
        self.total_level_height = 0
        self.platforms: List[Platform] = []

    def build(self) -> None:
        """
        Parses level files to convert level_char_codes into
        platform objects (pygame.Sprites).
        """
        line_number = 0

        with open(self.level_platforms_file) as fileobj:
            level_x = 0
            level_y = 0

            for line in fileobj:
                # removes whitespaces except spaces
                line_number += 1
                line = line.strip("\r\n\t")

                for i in range(0, len(line), DEFAULT_SPRITESHEET_LEVELS_CHARCODE_LENGTH):

                    level_char_code = line[
                        i : i + DEFAULT_SPRITESHEET_LEVELS_CHARCODE_LENGTH
                    ]  # reads the configured amount of characters

                    if len(level_char_code) != DEFAULT_SPRITESHEET_LEVELS_CHARCODE_LENGTH:
                        raise CorruptedLevelFile(
                            f"Corrupted file level code at line: {line_number}. Check the level file."
                        )

                    platform = self.level_char_code_to_platform(level_char_code, level_x, level_y)

                    if platform is not None:
                        self.platforms.append(platform)

                    level_x += self.platforms_width

                # gets total level width
                self.total_level_width = level_x

                # resets for next row
                level_x = 0
                level_y += self.platforms_height

            # gets total level height
            self.total_level_height = level_y

        if self.jazz_initial_x == -1 or self.jazz_initial_y == -1:
            raise MissingJazzInitialPositionOnLevelfile(
                "Unable to find jazz's initial position on the level. Check the map file."
            )

    @abstractmethod
    def level_char_code_to_platform(self, level_char_code, level_x, level_y) -> Optional[Platform]:
        """
        Abstract method for Mapping from level character to an actual pygame.Sprite object
        """
        pass
