"""
Module with the class representation
of Jazz's bullets.
"""
import os
from typing import Dict

import pygame
from jazzpy.interfaces.observable import ObserverMixin
from jazzpy.settings.general import PROJECT_ROOT_DIR
from jazzpy.settings.general import VIDEO_OPTIONS
from jazzpy.settings.hud import HUD_HEIGHT
from jazzpy.settings.hud import HUD_SPRITE
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
            os.path.join(PROJECT_ROOT_DIR, "jazzpy/sprites/misc/spritesheets/misc.png")
        )
        self.image = self.sprite_sheet.get_image(
            HUD_SPRITE, dimensions=(VIDEO_OPTIONS["screen_width"], HUD_HEIGHT)
        )

    def update(self, observable_state: Dict, observable_id: str):
        """
        Updates the HUD based on the observable states.
        """
        # TODO: Find a way to update the HUD sprite based on the received data
        print(f"Received an update: {observable_id}: {observable_state}")
