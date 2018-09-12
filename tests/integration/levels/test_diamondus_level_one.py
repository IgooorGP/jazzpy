"""
Module with integration tests for the diamondus level one.
"""

import os
import unittest
from unittest import mock

import pygame

from levels.diamondus.diamondus_level_one import DiamondusLevelOne


class DiamondusLevelOneTest(unittest.TestCase):
    """
    Integration tests for the Diamondus level one.
    """

    def setUp(self):
        pass

    @mock.patch("pygame.Surface")
    @mock.patch("levels.diamondus.diamondus_level_one.Platform")
    @mock.patch("levels.level.SpriteSheet")
    def test_parse_level(self, mocked_spritesheet, mocked_platform, mocked_surface):
        """
        Integration: DiamondusLevelOne: parse_level.
        """
        # mock creations
        mocked_img = mock.MagicMock()
        mocked_sheet = mock.MagicMock()
        mocked_sheet.get_image = mocked_img
        mocked_spritesheet.return_value = mocked_sheet
        mocked_surface.return_value.fill.return_value = mocked_img

        # mock returns
        mocked_plat = mock.MagicMock()
        mocked_platform.return_value = mocked_plat

        # method invocation
        level = DiamondusLevelOne("spritesheet", "dummy_level.txt", 40, 50)

        # expectations
        mocked_platform.assert_has_calls(
            [
                mock.call(0, 0, mocked_img),
                mock.call(40, 0, mocked_img),
                mock.call(80, 0, mocked_img),
                mock.call(0, 50, mocked_img),
                mock.call(40, 50, mocked_img),
                mock.call(80, 50, mocked_img),
                mock.call(0, 100, mocked_img),
                mock.call(40, 100, mocked_img),
                mock.call(80, 100, mocked_img),
            ]
        )

        self.assertEqual(level.total_level_width, 6 * 40)
        self.assertEqual(level.total_level_height, 4 * 50)
