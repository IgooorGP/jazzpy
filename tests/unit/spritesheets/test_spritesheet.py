"""
Module with unit tests for the SpriteSheet class.
"""
from unittest import mock

import pygame
import pytest
from jazzpy.exceptions.spritesheets import SpritesheetImpossibleMatrixColumnRequired
from jazzpy.exceptions.spritesheets import SpritesheetImpossibleMatrixRowRequired
from jazzpy.spritesheets.spritesheet import SpriteSheet


@mock.patch("jazzpy.spritesheets.spritesheet.pygame.transform.scale")
@mock.patch("jazzpy.spritesheets.spritesheet.pygame.Surface")
@mock.patch("jazzpy.spritesheets.spritesheet.pygame.image.load")
def test_should_get_pygame_surface_image_with_no_extra_dimensions(
    mocked_image_load, mocked_surface, mocked_scale
):
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


@mock.patch("jazzpy.spritesheets.spritesheet.pygame.transform.scale")
@mock.patch("jazzpy.spritesheets.spritesheet.pygame.Surface")
@mock.patch("jazzpy.spritesheets.spritesheet.pygame.image.load")
def test_should_get_pygame_surface_image_with_extra_dimensions(
    mocked_image_load, mocked_surface, mocked_scale
):
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


@mock.patch("jazzpy.spritesheets.spritesheet.pygame.image.load")
def test_should_compute_the_right_spritesheet_x_and_y(mocked_image_load):
    sprite_sheet = SpriteSheet("test", (10, 10), default_sprite_height=10, default_sprite_width=10)
    expected_x, expected_y = 40, 20

    # method invocation
    x, y = sprite_sheet._compute_spritesheet_location(spritesheet_row=4, spritesheet_col=2)

    assert x == expected_x
    assert y == expected_y


@mock.patch("jazzpy.spritesheets.spritesheet.pygame.image.load")
def test_should_compute_the_right_spritesheet_x_and_y_impossible_row(mocked_image_load):
    sprite_sheet = SpriteSheet("test", (10, 10), default_sprite_height=10, default_sprite_width=10)

    # method invocation
    with pytest.raises(SpritesheetImpossibleMatrixRowRequired):
        sprite_sheet._compute_spritesheet_location(spritesheet_row=-1, spritesheet_col=5)


@mock.patch("jazzpy.spritesheets.spritesheet.pygame.image.load")
def test_should_compute_the_right_spritesheet_x_and_y_impossible_row_too_big(mocked_image_load):
    sprite_sheet = SpriteSheet("test", (10, 10), default_sprite_height=10, default_sprite_width=10)

    # method invocation
    with pytest.raises(SpritesheetImpossibleMatrixRowRequired):
        sprite_sheet._compute_spritesheet_location(spritesheet_row=12, spritesheet_col=5)


@mock.patch("jazzpy.spritesheets.spritesheet.pygame.image.load")
def test_should_compute_the_right_spritesheet_x_and_y_impossible_row_type(mocked_image_load):
    sprite_sheet = SpriteSheet("test", (10, 10), default_sprite_height=10, default_sprite_width=10)

    # method invocation
    with pytest.raises(SpritesheetImpossibleMatrixRowRequired):
        sprite_sheet._compute_spritesheet_location(spritesheet_row="hi", spritesheet_col=5)


@mock.patch("jazzpy.spritesheets.spritesheet.pygame.image.load")
def test_should_compute_the_right_spritesheet_x_and_y_impossible_col(mocked_image_load):
    sprite_sheet = SpriteSheet("test", (10, 10), default_sprite_height=10, default_sprite_width=10)

    # method invocation
    with pytest.raises(SpritesheetImpossibleMatrixColumnRequired):
        sprite_sheet._compute_spritesheet_location(spritesheet_row=5, spritesheet_col=-10)


@mock.patch("jazzpy.spritesheets.spritesheet.pygame.image.load")
def test_should_compute_the_right_spritesheet_x_and_y_impossible_col_too_big(mocked_image_load):
    sprite_sheet = SpriteSheet("test", (10, 10), default_sprite_height=10, default_sprite_width=10)

    # method invocation
    with pytest.raises(SpritesheetImpossibleMatrixColumnRequired):
        sprite_sheet._compute_spritesheet_location(spritesheet_row=5, spritesheet_col=20)


@mock.patch("jazzpy.spritesheets.spritesheet.pygame.image.load")
def test_should_compute_the_right_spritesheet_x_and_y_impossible_col_type(mocked_image_load):
    sprite_sheet = SpriteSheet("test", (10, 10), default_sprite_height=10, default_sprite_width=10)

    # method invocation
    with pytest.raises(SpritesheetImpossibleMatrixColumnRequired):
        sprite_sheet._compute_spritesheet_location(spritesheet_row=5, spritesheet_col="whatever!")
