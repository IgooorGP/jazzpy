"""
Module with unit tests for the diamondus level one.
"""

from unittest import mock

from jazzpy.levels.diamondus.diamondus_level_one import DiamondusLevelOne


@mock.patch(
    "jazzpy.levels.diamondus.diamondus_level_one.DiamondusLevelOne.level_char_code_to_platform"
)
@mock.patch("jazzpy.levels.level.SpriteSheet")
def test_parse_level(mocked_SpriteSheet, mocked_level_char_code_to_platform):
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
    level = DiamondusLevelOne(
        "spritesheet", "./tests/resources/levels/test_level_parser.txt", "test", 40, 50
    )

    # to avoid exceptions
    level.jazz_initial_x = 0
    level.jazz_initial_y = 50

    level.build()

    # expectations
    mocked_level_char_code_to_platform.assert_has_calls(
        [
            mock.call("F1", 0, 0),
            mock.call("F1", 40, 0),
            mock.call("F1", 80, 0),
            mock.call("  ", 0, 50),
            mock.call("  ", 40, 50),
            mock.call("F1", 80, 50),
            mock.call("T1", 0, 100),
            mock.call("T1", 40, 100),
            mock.call("T1", 80, 100),
        ]
    )

    assert level.total_level_width == 3 * 40
    assert level.total_level_height == 3 * 50
