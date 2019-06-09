"""
Module with the class representation
of Jazz's bullets.
"""
import os
from typing import Dict
from typing import Tuple

import pygame
from jazzpy.interfaces.observable import ObserverMixin
from jazzpy.settings.general import PROJECT_ROOT_DIR
from jazzpy.settings.general import VIDEO_OPTIONS
from jazzpy.settings.hud import DEFAULT_SPRITESHEET_GOLDEN_NUMBER_DIMENSIONS
from jazzpy.settings.hud import GOLDEN_NUMBERS_ON_SCREEN_DIMENSIONS
from jazzpy.settings.hud import HUD_HEIGHT
from jazzpy.settings.hud import HUD_SPRITESHEET_POSITION
from jazzpy.settings.jazz import JAZZ_OBSERVABLE_ID
from jazzpy.support.spritesheet import SpriteSheet


class Hud(pygame.sprite.Sprite, ObserverMixin):
    """
    HUD of the game which is an observer of the Jazz state.
    """

    def __init__(self):
        """
        Default constructor for the bullets.
        """
        super().__init__()

        # default position
        self.sprite_sheet = SpriteSheet(
            os.path.join(PROJECT_ROOT_DIR, "jazzpy/sprites/misc/spritesheets/hud.png")
        )

        self.golden_numbers_spritesheet = SpriteSheet(
            os.path.join(PROJECT_ROOT_DIR, "jazzpy/sprites/misc/spritesheets/golden_numbers.png"),
            spritesheet_matrix_dimensions=(0, 11),
            default_sprite_width=DEFAULT_SPRITESHEET_GOLDEN_NUMBER_DIMENSIONS["width"],
            default_sprite_height=DEFAULT_SPRITESHEET_GOLDEN_NUMBER_DIMENSIONS["height"],
        )

        self.image = self.sprite_sheet.get_image(
            HUD_SPRITESHEET_POSITION, dimensions=(VIDEO_OPTIONS["screen_width"], HUD_HEIGHT)
        )

    @classmethod
    def get_position(cls) -> Tuple[int, int]:
        return 0, VIDEO_OPTIONS["screen_height"] - HUD_HEIGHT

    def _get_golden_number_image(self, number, width=None, height=None) -> pygame.Surface:
        if width is None:
            width = GOLDEN_NUMBERS_ON_SCREEN_DIMENSIONS["width"]

        if height is None:
            height = GOLDEN_NUMBERS_ON_SCREEN_DIMENSIONS["height"]

        golden_number_image_surface = self.golden_numbers_spritesheet.get_image_by_row_and_col(
            0, number, dimensions=(width, height)
        )

        return golden_number_image_surface

    def update(self, observable_state: Dict, observable_id: str):
        """
        Updates the HUD based on the observable states.
        """
        if observable_id == JAZZ_OBSERVABLE_ID:
            jazz_lives = observable_state.get("lives")
            self.image.blit(self._get_golden_number_image(jazz_lives), dest=(10, 10))
