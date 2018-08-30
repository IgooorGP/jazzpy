"""
Module with the class representation
of Jazz the Jack Rabbit.
"""
import pygame
from sprites.spritesheet import SpriteSheet


class Jazz(pygame.sprite.Sprite):
    """
    Jazz's class.
    """

    # http://getspritexy.com/
    DEFAULT_POSITION_SPRITE = (16, 22, 37, 37)

    WALKING_SPRITE_1 = (16, 60, 37, 37)
    WALKING_SPRITE_2 = (53, 59, 37, 37)
    WALKING_SPRITE_3 = (87, 59, 37, 37)
    WALKING_SPRITE_4 = (121, 58, 37, 37)
    WALKING_SPRITE_5 = (155, 58, 37, 37)
    WALKING_SPRITE_6 = (191, 58, 37, 37)

    RUNNING_SRITE_1 = (16, 95, 37, 36)
    RUNNING_SRITE_2 = (54, 95, 37, 37)
    RUNNING_SRITE_3 = (87, 95, 37, 37)
    RUNNING_SRITE_4 = (125, 95, 37, 37)
    RUNNING_STOP_SPRITE_1 = (160, 95, 37, 37)

    SHOOTING_SPRITE_1 = (157, 130, 37, 37)

    LOOKING_DOWN_SPRITE_1 = (88, 131, 37, 37)
    LOOKING_UP_SPRITE_1 = (15, 131, 37, 37)

    JUMPING_UP_SPRITE_1 = (16, 207, 37, 37)
    GOING_DOWN_SPRITE_1 = (52, 207, 37, 37)

    HURT_SPRITE_1 = (159, 245, 37, 37)
    HURT_SPRITE_2 = (194, 244, 37, 37)
    HURT_SPRITE_3 = (230, 244, 37, 37)

    MAX_SPEED_X = 2

    def __init__(self):
        """
        Default constructor for the Jazz JackRabbit character class.
        """
        # super class init
        super().__init__()

        # loads the sprite_sheet
        self.sprite_sheet = SpriteSheet("./sprites/jazz/jazz.png")

        # jazz default position
        self.x, self.y = 0, 0
        self.speed_x, self.speed_y = 0, 0

        # jazz imgs
        self.image = self.sprite_sheet.get_image(self.DEFAULT_POSITION_SPRITE)
        self.rect = self.image.get_rect(
            topleft=(self.x, self.y)  # gets width/height of the img but x, y == 0, 0 always!
        )

        self._K_d_pressed = False
        self._K_a_pressed = False
        self.is_jumping = False

    def move(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self._K_d_pressed = True

            if event.key == pygame.K_a:
                self._K_a_pressed = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self._K_d_pressed = False

            if event.key == pygame.K_a:
                self._K_a_pressed = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self._K_d_pressed = False

    def update(self):
        """
        Updates the current position. Checks for collisions. Listen to events.
        """
        if self._K_d_pressed:
            self.speed_x += 0.5
            self.speed_x = self.MAX_SPEED_X if self.speed_x > self.MAX_SPEED_X else self.speed_x

        elif self._K_a_pressed:
            self.speed_x -= 0.5
            self.speed_x = -self.MAX_SPEED_X if self.speed_x < self.MAX_SPEED_X else self.speed_x

        else:
            if self.speed_x > 0:
                self.speed_x -= 0.5
                self.speed_x = 0 if self.speed_x < 0 else self.speed_x

            if self.speed_x < 0:
                self.speed_x += 0.5
                self.speed_x = 0 if self.speed_x > 0 else self.speed_x

        self.rect.x += self.speed_x
        if self.speed_x > 1.5:
            self.image = self.sprite_sheet.get_image(self.RUNNING_SRITE_1)

        if self.speed_x == 0:
            self.image = self.sprite_sheet.get_image(self.DEFAULT_POSITION_SPRITE)

        # keystate = pygame.key.get_pressed()

        # if keystate[pygame.K_d]:
        #     self.speed_x += 1
        # else:
        #     if self.speed_x >= 1:
        #         self.speed_x -= 1
        # self.rect.x += self.speed_x
