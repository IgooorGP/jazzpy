"""
This module contains the Camera class
to apply offsets to the screen entities
in order to generate a scroll effect.
"""
import pygame


class Camera:
    """
    Class to apply offsets to screen entities.
    """

    def __init__(self, screen_width, screen_height, level_width, level_height):
        """
        Default constructor for a camera object.

        Args:
            camera_fn (function): camera function.
            width (int): total width of the level
            height (int): total height of the level
        """
        # holds the camera state
        self.camera_x = 0
        self.camera_y = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.level_width = level_width
        self.level_height = level_height

    def apply(self, target) -> pygame.Rect:
        """
        Re-calculates the position of an entity on the
        screen in order to apply the scrolling effect.
        """
        # gives an offset to the entity based on camera_x and camera_y
        return target.rect.move(self.camera_x, self.camera_y)

    def update(self, target) -> None:
        """
        Updates the camera position by following an entity (player).
        """
        self.camera_x = int(self.screen_width / 2) - target.rect.x
        self.camera_y = int(self.screen_height / 2) - target.rect.y

        self.camera_x = min(0, self.camera_x)  # stop scrolling at the left edge
        self.camera_x = max(-(self.level_width - self.screen_width), self.camera_x)  # stop scrolling at the right edge
        self.camera_y = max(-(self.level_height - self.screen_height), self.camera_y)  # stop scrolling at the bottom
        self.camera_y = min(0, self.camera_y)  # stop scrolling at the top
