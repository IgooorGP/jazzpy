"""
Module with unit tests for the SpriteSheet class.
"""

import unittest
from unittest import mock

import pygame

from sprites.spritesheet import SpriteSheet


class SpriteSheeTest(unittest.TestCase):
    """
    Unit tests for the SpriteSheet class.
    """

    def setUp(self):
        pass

    @mock.patch("sprites.spritesheet.pygame.transform.scale")
    @mock.patch("sprites.spritesheet.pygame.Surface")
    @mock.patch("sprites.spritesheet.pygame.image.load")
    def test_get_image_no_dimensions(self, mocked_image_load, mocked_surface, mocked_scale):
        """
        Unit: SpriteSheet: tests get_image when no dimensions
              tuple are passed as an argument.
        """
        # mock definitions
        mocked_sheet = mock.MagicMock()
        mocked_image_load.return_value.convert_alpha.return_value = mocked_sheet

        mocked_image = mock.MagicMock()
        mocked_surface.return_value = mocked_image

        # method invocation
        sprite_sheet = SpriteSheet("test")
        sprite_sheet.get_image((1, 1, 10, 10))

        # mock assertions
        mocked_surface.assert_called_once_with((10, 10), pygame.SRCALPHA)
        mocked_image.blit.assert_called_once_with(mocked_sheet, dest=(0, 0), area=(1, 1, 10, 10))
        mocked_scale.assert_not_called()

    @mock.patch("sprites.spritesheet.pygame.transform.scale")
    @mock.patch("sprites.spritesheet.pygame.Surface")
    @mock.patch("sprites.spritesheet.pygame.image.load")
    def test_get_image_with_dimensions(self, mocked_image_load, mocked_surface, mocked_scale):
        """
        Unit: SpriteSheet: tests get_image with sprite dimensions.
        """
        # mock definitions
        mocked_sheet = mock.MagicMock()
        mocked_image_load.return_value.convert_alpha.return_value = mocked_sheet

        mocked_image = mock.MagicMock()
        mocked_surface.return_value = mocked_image

        # method invocation
        sprite_sheet = SpriteSheet("test")
        sprite_sheet.get_image((1, 1, 10, 10), dimensions=(50, 50))

        # mock assertions
        mocked_surface.assert_called_once_with((10, 10), pygame.SRCALPHA)
        mocked_image.blit.assert_called_once_with(mocked_sheet, dest=(0, 0), area=(1, 1, 10, 10))
        mocked_scale.assert_called_once_with(mocked_image, (50, 50))
