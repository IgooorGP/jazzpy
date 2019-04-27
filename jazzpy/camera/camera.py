"""
This module contains the Camera class to apply offsets to the
screen entities in order to generate a scroll effect.

The camera itself, is just a Rectangle whose width is the screen
width and the height is the screen height (minus a HUD, etc.).

It's main function is to compute an offset based on the player's
updated coordinates in order to "drag" him back to the center
of the screen and to apply the same offset to all objects that
must be displayed on the screen.

Example for the x axis offset calculation:

                Coordinate System
  x ---------> x
  |
  |    . (x,y)
  |
  v
y

Initial player state at the center of the screen @ (x1,y1):

    <------------ screen size ------------>
  + ---------------- Camera --------------- +
  |											|
  |					  			     		|
  |					    (player)       		|
h |					  p (x1,y1) 		    |
  |	                                    	|
  | 										|
  |											|
  + --------------------------------------- +

    <------------ screen size ------------>
  + ---------------- Camera --------------- +
  |											|
  |					  			     		|
  |					     					|
h |					  . (center)		    |
  |	                                    	|
  | 										|
  |											|
  + --------------------------------------- +

After computing the updated player position's (x2,y2):

    <------------ screen size ------------>
  + ---------------- Camera --------------- +
  |		        x2 				(x2,y2)		|
  |--------------------------- p    		|
  |					     					|
h |					   .             	    |
  |	-------------------  <---->            	|
  |   screen_width/2	 offset_x			|
  | 										|
  |											|
  + --------------------------------------- + 

The offset_y computation is analogous.
"""
import pygame


class Camera:
    """
    Class to apply offsets to player and other screen objects and sprites.
    """

    def __init__(self, screen_width: int, screen_height: int, level_width: int, level_height: int):
        """
        Default constructor for a camera object.

        Args:
            screen_width (int): game's screen width.
            screen_height (int): game's screen height.
            level_width (int): total width of the level.
            level_height (int): total height of the level.
        """
        # holds the initial camera position
        self.offset_x = 0
        self.offset_y = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.level_width = level_width
        self.level_height = level_height

    def apply_offset(self, target: pygame.sprite.Sprite) -> pygame.Rect:
        """
        Applies an offset to the target rectangle in order to centralize the
        player and display all the objects in a corrected position where the
        player is at the center of the camera.

        [!]: In order for this method to work, the new target postion (state)
             M U S T already have been UPDATED, e.g., new x, y coords must
            already have been calculated.

        Args:
            target (object): Any object that has a rect attribute that must
                             be blitted in the corrected position of the
                             camera.

        Returns:
            (pygame.Rect): Moved rectangle due to the camera x, y offset.
        """
        return target.rect.move(self.offset_x, self.offset_y)

    def compute_offset(self, center_target: pygame.sprite.Sprite) -> None:
        """
        Computes a new offset to be applied to all objects on the camera in
        order to centralize the player at the center and to make other objects
        appear at corrected positions according to the new centralized player
        position.

        [!]: This offset is used to "push" the player back to the center of the
             camera and, in the same fashion, the other game sprites on the
             screen.

        Args:
            center_target (pygame.sprite.Sprite): Player object which will
            used to compute the camera offset in order to centralize it and
            correct every other sprite position. It's the sprite which will
            be used to centralize every other position.
        """
        # centers the camera based on the target that it is following
        self.offset_x = -(center_target.rect.x - int(self.screen_width / 2))
        self.offset_y = -(center_target.rect.y - int(self.screen_height / 2))

        # avoid showing black parts beyond the level
        self.offset_x = min(0, self.offset_x)  # stop scrolling at the left edge
        self.offset_x = max(
            -(self.level_width - self.screen_width), self.offset_x
        )  # stop scrolling at the right edge
        self.offset_y = max(
            -(self.level_height - self.screen_height), self.offset_y
        )  # stop scrolling at the bottom
        self.offset_y = min(0, self.offset_y)  # stop scrolling at the top
