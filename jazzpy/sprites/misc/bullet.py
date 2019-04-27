"""
Module with the class representation
of Jazz's bullets.
"""
import os

import pygame
from jazzpy.config.settings import GAME_ROOT_DIR
from jazzpy.spritesheets.spritesheet import SpriteSheet


class Bullet(pygame.sprite.Sprite):
    """
    Bullet class.
    """

    BLASTER_SPRITE = (598, 606, 10, 10)
    TOASTER_SPRITE = (613, 602, 25, 25)

    EXPLOSION_SPRITES = (
        (491, 972, 25, 25),
        (518, 972, 25, 25),
        (544, 972, 25, 25),
        (575, 972, 25, 25),
    )

    BULLET_SPEED = 15  # cannot be a float (gets truncated)

    def __init__(self, level_x, level_y, direction):
        """
        Default constructor for the bullets.
        """
        super().__init__()

        # default position
        self.sprite_sheet = SpriteSheet(os.path.join(GAME_ROOT_DIR, "spritesheets/misc/misc.png"))
        self.direction = direction
        self.x, self.y = level_x, level_y
        self.has_hit = False

        # bullet img
        self.image = self.sprite_sheet.get_image(self.BLASTER_SPRITE)
        self.rect = self.image.get_rect(center=(self.x, self.y))

        if self.direction == "right":
            self.speed = self.BULLET_SPEED
        else:
            self.speed = -self.BULLET_SPEED

    def update(self, platforms):
        """
        Updates bullet position.
        """
        if self.direction == "right":
            self.rect.right += self.BULLET_SPEED
        else:
            self.rect.left -= self.BULLET_SPEED

        self.collide(self.speed, 0, platforms)

    def collide(self, speed_x, speed_y, platforms):
        """ Detects x-y collisions. """
        for platform in platforms:

            if pygame.sprite.collide_rect(self, platform):

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
        self.image = self.sprite_sheet.get_image(self.EXPLOSION_SPRITES[0])
        self.rect = self.rect.move(-10, -10)  # offset to centralize the shoot image
