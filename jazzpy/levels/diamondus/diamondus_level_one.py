"""
Module with the concrete implementation of the
first level of the Diamondus world.
"""
from jazzpy.levels.level import Level
from jazzpy.sprites.platforms.platforms import Platform


class DiamondusLevelOne(Level):
    """
    Concrete implementation of the abstract class Level
    for the first stage of the game of the Diamondus world.
    """

    # has platforms_width and height
    # has sprite_sheet object
    # has platforms list
    T1 = (32, 193, 32, 32)  # T1

    # fill sprites
    F1 = (64, 416, 32, 32)  # standard fill
    F2 = (96, 193, 32, 32)  # small diamonds
    F3 = (63, 225, 26, 29)  # red diamond
    F4 = (38, 226, 26, 29)  # teal diamond
    F5 = (2, 226, 26, 29)  # green diamond
    F6 = (193, 353, 31, 31)  # pre ramp left <-
    F0 = (161, 354, 29, 30)  # pre ramp right ->
    F7 = (167, 293, 51, 51)  # full diamonds
    F8 = (99, 286, 28, 30)  # F8 right
    F9 = (4, 320, 28, 28)  # F9  left

    R1 = (257, 352, 31, 31)  # R1 down ramp
    R2 = (96, 352, 32, 30)  # U1  up ramp

    C1 = (129, 224, 26, 27)  # corner left /
    C2 = (101, 288, 27, 30)  # corner right \

    EDGE_GRASS_SPRITE_LEFT_1 = (164, 191, 28, 32)  # E1
    EDGE_GRASS_SPRITE_RIGHT_1 = (219, 192, 28, 32)  # E2

    def level_char_code_to_platform(self, level_char_code, level_x, level_y):
        """
        Non-abstract implementation of the method that converts level_char_codes
        into Platform objects at the right positions of the level.
        """
        platform_dimensions = (self.platforms_width, self.platforms_height)

        class_vars = {k: getattr(self, k) for k in dir(self) if not k.startswith("__")}

        sprite_tuple = class_vars.get(level_char_code)

        if sprite_tuple:
            image = self.sprite_sheet.get_image(sprite_tuple, dimensions=platform_dimensions)

            return Platform(level_x, level_y, image)

        # sprite tuple was not found
        if level_char_code == "JJ":
            self.jazz_initial_x, self.jazz_initial_y = level_x, level_y

        return None
