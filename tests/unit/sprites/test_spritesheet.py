"""
Module with unit tests for the SpriteSheet class.
"""

import unittest
import pygame

from unittest import mock
from sprites.spritesheet import SpriteSheet


class SpriteSheeTest(unittest.TestCase):
    """
    Unit tests for the SpriteSheet class.
    """

    def setUp(self):
        self.spritesheet = SpriteSheet("test")

    @mock("sprites.spritesheet.pygame.Surface")
    def test_get_image_no_dimensions(self, mocked_surface):
        """
        Unit: SpriteSheet: tests get_image when no dimensions
              tuple are passed as an argument.
        """
        spritesheet_locations = (1, 1, 10, 10)

        # expectations
        mocked_image = mock.MagicMock(spec=py)
        mocked_surface.return_value = 

        # method invocation
        self.spritesheet.get_image()
