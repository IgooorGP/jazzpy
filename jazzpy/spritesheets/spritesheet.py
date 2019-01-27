"""
Module with a convenience class to get
images from a spritesheet.
"""
import pygame


class SpriteSheet:
    """
    Class that handles getting images from a spritesheet.
    """

    def __init__(self, file_name):
        """
        Default constructor.

        Args:
            file_name(str): relative os.path based on jazz.py file.
        """
        # playing jazz = https://classicreload.com/jazz-jackrabbit.html
        # removing background spritesheet = https://www141.lunapic.com/editor/
        # get spritesheet positions = http://getspritexy.com/

        # loads the whole sprite sheet image onto a pygame.Surface
        self.sprite_sheet = pygame.image.load(file_name).convert_alpha()

    def get_image(self, spritesheet_locations, dimensions=None):
        """
        Returns a pygame.Surface object with a blit image from
        a spritesheet. Stretches the image if the width, height of
        the image at the spritesheet is smaller than the desired
        dimensions.

        Args:
            at (tuple): tuple with the following data: x, y, sprite_width, sprite_height.
            dimensions (tuple): tuple with the size of the image

        Returns:
            (pygame.Surface): Blited surface (image).
        """
        # reads the img position at the sprite sheet
        spritesheet_x, spritesheet_y, sprite_width, sprite_height = spritesheet_locations

        if dimensions:
            # unpacks dimensions of the final surface
            image_width, image_height = dimensions
        else:
            # if no dimensions are given we assume its the same as the spritesheet
            image_width, image_height = sprite_width, sprite_height

        # creates an empty surface
        image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)

        # blits the sprite_sheet surface at the position dest=(0, 0) of the empty surface
        # area specifies the cropped (smaller portion) of the sprite_sheet
        image.blit(
            self.sprite_sheet,
            dest=(0, 0),
            area=(spritesheet_x, spritesheet_y, sprite_width, sprite_height),
        )

        # if the desired image width is bigger than the sprite width, resize to the desired img size
        if image_width > sprite_width and image_height > sprite_height:
            return pygame.transform.scale(image, (image_width, image_height))

        return image
