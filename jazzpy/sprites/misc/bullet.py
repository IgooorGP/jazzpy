"""
Module with the class representation of Jazz's bullets.
"""
import os

import pygame
from jazzpy.settings.bullet import BLASTER_SPRITE
from jazzpy.settings.bullet import BULLET_SPEED
from jazzpy.settings.bullet import EXPLOSION_SPRITES
from jazzpy.settings.general import PROJECT_ROOT_DIR
from jazzpy.support.spritesheet import SpriteSheet


class Bullet(pygame.sprite.Sprite):
    """
    Bullet class.
    """

    def __init__(self, level_x, level_y, direction):
        """
        Default constructor for the bullets.
        """
        super().__init__()

        # default position
        self.sprite_sheet = SpriteSheet(
            os.path.join(PROJECT_ROOT_DIR, "jazzpy/sprites/misc/spritesheets/misc.png")
        )
        self.direction = direction
        self.x, self.y = level_x, level_y
        self.has_hit = False

        # bullet img
        self.image = self.sprite_sheet.get_image(BLASTER_SPRITE)
        self.rect = self.image.get_rect(center=(self.x, self.y))

        if self.direction == "right":
            self.speed = BULLET_SPEED
        else:
            self.speed = -BULLET_SPEED

    def update(self, platforms):
        """
        Updates bullet position.
        """
        if self.direction == "right":
            self.rect.right += BULLET_SPEED
        else:
            self.rect.left -= BULLET_SPEED

        self.collide(self.speed, 0, platforms)

    def collide(self, speed_x, speed_y, platforms):
        """ Detects x-y collisions. """
        for platform in platforms:

            if pygame.sprite.collide_rect(self, platform) and platform.is_collidable:

                if speed_x > 0:

                    self.rect.right = platform.rect.left
                    self.has_hit = True

                if speed_x < 0:

                    self.rect.left = platform.rect.right
                    self.has_hit = True

                self._change_sprite()

    def _change_sprite(self):
        """
        Changes Jazz's bullets explosion sprites.
        """
        self.image = self.sprite_sheet.get_image(EXPLOSION_SPRITES[0])
        self.rect = self.rect.move(-10, -10)  # offset to centralize the shoot image
