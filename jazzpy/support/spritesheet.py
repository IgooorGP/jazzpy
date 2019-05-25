"""
Module with a convenience class to get
images from a spritesheet.
"""
from typing import Tuple

import pygame
from jazzpy.config.settings import DEFAULT_SPRITESHEET_TILE_DIMENSIONS
from jazzpy.exceptions.spritesheets import SpritesheetImpossibleMatrixColumnRequired
from jazzpy.exceptions.spritesheets import SpritesheetImpossibleMatrixRowRequired
from jazzpy.exceptions.spritesheets import SpritesheetMatrixDimensionsNotConfigured


class SpriteSheet:
    """
    Class that handles getting images from a spritesheet.
    """

    def __init__(
        self,
        file_name: str,
        spritesheet_matrix_dimensions: Tuple[int, int] = None,
        default_sprite_width: int = DEFAULT_SPRITESHEET_TILE_DIMENSIONS["width"],
        default_sprite_height: int = DEFAULT_SPRITESHEET_TILE_DIMENSIONS["height"],
    ):
        """
        Default constructor.

        Args:
            file_name (str): relative os.path based on jazz.py file.
            default_sprite_width (int): default width for the generate pygame.Surfaces;
            default_sprite_height (int): default width for the generate pygame.Surfaces;
        """
        # loads the whole sprite sheet image onto a pygame.Surface
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()
        self.default_sprite_width = default_sprite_width
        self.default_sprite_height = default_sprite_height
        self.spritesheet_matrix_dimensions = spritesheet_matrix_dimensions

    def _compute_spritesheet_location(
        self, spritesheet_row: int, spritesheet_col: int
    ) -> Tuple[int, int]:
        """
        Computes the spritesheet x,y coordinates based on a given row and column of a fixed
        width and height spritesheet. Raises exceptions if an impossible row or column is supplied.
        Rows and columns are ZERO based.

        Args:
            spritesheet_row (int): the zero-based row of the spritesheet matrix.
            spritesheet_col (int): the zero-based col of the spritesheet matrix.

        Returns:
            tuple: tuple of the x,y coordinates where the sprite to be collected is.

           (0,0) ----> x
           |
           |/
           y
        """
        if self.spritesheet_matrix_dimensions is None:
            raise SpritesheetMatrixDimensionsNotConfigured(
                "Impossible to compute location without matrix dimensions."
            )

        if not isinstance(spritesheet_row, int):
            raise SpritesheetImpossibleMatrixRowRequired(
                f"Impossible asked row value: {spritesheet_row}, not an int!"
            )

        if not isinstance(spritesheet_col, int):
            raise SpritesheetImpossibleMatrixColumnRequired(
                f"Impossible asked col value: {spritesheet_col}, not an int!"
            )

        if spritesheet_row < 0 or spritesheet_row > self.spritesheet_matrix_dimensions[0]:
            raise SpritesheetImpossibleMatrixRowRequired(
                f"Impossible asked row value: {spritesheet_row}, dimensions: {self.spritesheet_matrix_dimensions}"
            )

        if spritesheet_col < 0 or spritesheet_col > self.spritesheet_matrix_dimensions[1]:
            raise SpritesheetImpossibleMatrixColumnRequired(
                f"Impossible asked col value: {spritesheet_col}, dimensions: {self.spritesheet_matrix_dimensions}"
            )

        spritesheet_x = spritesheet_col * self.default_sprite_width
        spritesheet_y = spritesheet_row * self.default_sprite_height

        return spritesheet_x, spritesheet_y

    def get_image(self, spritesheet_locations: Tuple, dimensions: Tuple = None) -> pygame.Surface:
        """
        Returns a pygame.Surface object with a blit image from
        a spritesheet. Stretches the image if the width, height of
        the image at the spritesheet is smaller than the desired
        dimensions.

        Args:
            spritesheet_locations (tuple): tuple with the following data: x, y, sprite_width, sprite_height.
            dimensions (tuple): tuple with the size of the image

        Returns:
            (pygame.Surface): Blited surface (image).
        """
        # reads the img position at the sprite sheet
        spritesheet_x, spritesheet_y, sprite_width, sprite_height = spritesheet_locations

        if dimensions:
            # unpacks dimensions of the final surface
            image_width, image_height = dimensions
        else:
            # if no dimensions are given we assume its the same as the spritesheet
            image_width, image_height = sprite_width, sprite_height

        # creates an empty surface
        image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)

        # blits the sprite_sheet surface at the position dest=(0, 0) of the empty surface
        # area specifies the cropped (smaller portion) of the sprite_sheet
        image.blit(
            self.sprite_sheet,
            dest=(0, 0),
            area=(spritesheet_x, spritesheet_y, sprite_width, sprite_height),
        )

        # if the desired image width is bigger than the sprite width, resize to the desired img size
        if image_width > sprite_width and image_height > sprite_height:
            return pygame.transform.scale(image, (image_width, image_height))

        return image

    def get_image_by_row_and_col(
        self, spritesheet_row: int, spritesheet_col: int, dimensions: Tuple = None
    ) -> pygame.Surface:
        """
        In this method, the spritesheet is treated as a
        zero-based MATRIX with fixed width and height sprites that can
        be "sliced". It computes, based on a given row and col, the appropriate
        spritesheet x and y and runs the ordinary get_image method.

        Args:
            spritesheet_row (int): row of the zero-based spritesheet matrix;
            spritesheet_col (int): row of the zero-based spritesheet matrix;
            dimensions (tuple): tuple with the size of the image

        Returns:
            (pygame.Surface): Blited surface (image).
        """
        # reads the img position at the sprite sheet
        spritesheet_x, spritesheet_y = self._compute_spritesheet_location(
            spritesheet_row, spritesheet_col
        )

        return self.get_image(
            (spritesheet_x, spritesheet_y, self.default_sprite_width, self.default_sprite_height),
            dimensions,
        )
