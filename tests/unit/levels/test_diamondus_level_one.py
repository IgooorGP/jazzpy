"""
Module with unit tests for the diamondus level one.
"""

import unittest
from unittest import mock

from levels.diamondus.diamondus_level_one import DiamondusLevelOne


class DiamondusLevelOneTest(unittest.TestCase):
    """
    Unit tests for the Diamondus level one.
    """

    def setUp(self):
        pass

    @mock.patch("levels.diamondus.diamondus_level_one.DiamondusLevelOne.level_char_code_to_platform")
    @mock.patch("levels.level.SpriteSheet")
    def test_parse_level(self, mocked_SpriteSheet, mocked_level_char_code_to_platform):
        """
        Unit: DiamondusLevelOne: tests parse_level with dummy level txt.
        """
        # mock creations
        mocked_img = mock.MagicMock()
        mocked_sheet = mock.MagicMock()
        mocked_SpriteSheet.return_value = mocked_sheet

        # mock returns
        mocked_level_char_code_to_platform.return_value = mocked_img

        # method invocation
        level = DiamondusLevelOne("spritesheet", "./tests/unit/levels/test_level_parser.txt", 40, 50)

        # to avoid exceptions
        level.jazz_initial_x = 0
        level.jazz_initial_y = 50

        level.build()

        # expectations
        mocked_level_char_code_to_platform.assert_has_calls(
            [
                mock.call("F", 0, 0),
                mock.call("F", 40, 0),
                mock.call("F", 80, 0),
                mock.call(" ", 0, 50),
                mock.call(" ", 40, 50),
                mock.call("F", 80, 50),
                mock.call("T", 0, 100),
                mock.call("T", 40, 100),
                mock.call("T", 80, 100),
            ]
        )

        self.assertEqual(level.total_level_width, 3 * 40)
        self.assertEqual(level.total_level_height, 3 * 50)

    @mock.patch("levels.diamondus.diamondus_level_one.Platform")
    @mock.patch("pygame.Surface")
    @mock.patch("levels.level.SpriteSheet")
    def test_level_char_code_to_platform(self, mocked_SpriteSheet, mocked_Surface, mocked_Platform):
        """
        Unit: DiamondousLevelOne: tests level_char_code method.
        """
        # mock returns
        mocked_image = mock.MagicMock()
        mocked_SpriteSheet.return_value.get_image.return_value = mocked_image
        # mocked_surface_image = mock.MagicMock()
        # mocked_Surface.return_value.fill.return_value = mocked_surface_image

        # method invocation
        level = DiamondusLevelOne("spritesheet", "./tests/unit/levels/test_level_parser.txt", 40, 50)
        level.level_char_code_to_platform("F", 50, 50)
        level.level_char_code_to_platform("T", 100, 100)
        level.level_char_code_to_platform(" ", 200, 200)

        # mock assertions
        mocked_Platform.assert_has_calls(
            [
                mock.call(50, 50, mocked_image),
                mock.call(100, 100, mocked_image),
                # mock.call(200, 200, mocked_surface_image),
            ]
        )
