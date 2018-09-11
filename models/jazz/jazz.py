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

    RUNNING_SPRITES = (RUNNING_SRITE_1, RUNNING_SRITE_2, RUNNING_SRITE_3, RUNNING_SRITE_4)

    RUNNING_STOP_SPRITE_1 = (160, 95, 37, 37)

    SHOOTING_SPRITE_1 = (157, 130, 37, 37)

    LOOKING_DOWN_SPRITE_1 = (88, 131, 37, 37)
    LOOKING_UP_SPRITE_1 = (15, 131, 37, 37)

    JUMPING_SPRITE_1 = (16, 207, 37, 37)
    FALLING_SPRITE_1 = (52, 207, 37, 37)

    HURT_SPRITE_1 = (159, 245, 37, 37)
    HURT_SPRITE_2 = (194, 244, 37, 37)
    HURT_SPRITE_3 = (230, 244, 37, 37)

    MAX_SPEED_X = 4
    ACCELERATION_X = 0.1
    INITIAL_JUMP_Y_SPEED = 10  # y coord is negative!
    GRAVITY_SPEED = 0.5

    def __init__(self, level_x, level_y):
        """
        Default constructor for the Jazz JackRabbit character class.
        """
        # super class init
        super().__init__()

        # loads the sprite_sheet
        self.sprite_sheet = SpriteSheet("./sprites/jazz/jazz.png")

        # jazz default position
        self.x, self.y = level_x, level_y
        self.speed_x, self.speed_y = 0, 0
        self.accerelation_x, self.acceleration_y = 0, 0

        # jazz imgs
        self.image = self.sprite_sheet.get_image(self.DEFAULT_POSITION_SPRITE)
        self.rect = self.image.get_rect(
            topleft=(self.x, self.y)  # gets width/height of the img but the position is at x, y
        )

        self._K_d_pressed = False
        self._K_a_pressed = False
        self.is_jumping = False
        self.is_falling = False
        self.is_on_floor = True
        self.jazz_orientation = "right"
        self.current_running_sprite = 0

    def get_running_sprite(self):
        """
        Alters Jazz's running sprite on every frame to give a 
        movement sensation.
        """

        tpl_sprite = self.RUNNING_SPRITES[self.current_running_sprite]

        self.current_running_sprite += 1
        self.current_running_sprite = 0 if self.current_running_sprite > 3 else self.current_running_sprite

        return tpl_sprite

    def change_sprite(self):
        """ 
        Performs sprite changes based on Jazz's movements. 
        """
        if abs(self.speed_x) > 0 and abs(self.speed_x) < 0.4:
            self.image = self.sprite_sheet.get_image(self.WALKING_SPRITE_1)

        if abs(self.speed_x) >= 0.4 and abs(self.speed_x) < 0.8:
            self.image = self.sprite_sheet.get_image(self.WALKING_SPRITE_2)

        if abs(self.speed_x) >= 0.8 and abs(self.speed_x) < 1.2:
            self.image = self.sprite_sheet.get_image(self.WALKING_SPRITE_3)

        if abs(self.speed_x) >= 1.2 and abs(self.speed_x) < 1.5:
            self.image = self.sprite_sheet.get_image(self.WALKING_SPRITE_4)

        if abs(self.speed_x) >= 2:
            # self.image = self.sprite_sheet.get_image(self.RUNNING_SRITE_1)
            self.image = self.sprite_sheet.get_image(self.get_running_sprite())

        if self.speed_x == 0:
            self.image = self.sprite_sheet.get_image(self.DEFAULT_POSITION_SPRITE)

        if self.is_jumping:
            self.image = self.sprite_sheet.get_image(self.JUMPING_SPRITE_1)

        if self.is_falling:
            self.image = self.sprite_sheet.get_image(self.FALLING_SPRITE_1)

        # always, in the end, change flip the sprite
        if self.jazz_orientation == "left":
            self.image = pygame.transform.flip(self.image, True, False)

    def capture_event(self, event):
        """
        Handles pygame.events to update Jazz's attributes. 
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT and self.is_on_floor:  # jumps only when at the floor
                self.is_jumping = True
                self.is_on_floor = False
                self.is_falling = False
                self.speed_y = -self.INITIAL_JUMP_Y_SPEED  # negative for moving up!

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self._K_d_pressed = True
                self.jazz_orientation = "right"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self._K_a_pressed = True
                self.jazz_orientation = "left"

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self._K_d_pressed = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self._K_a_pressed = False

    def update(self):
        """
        Updates the current position. Checks for collisions. Listen to events.
        """
        # x movement
        if self._K_d_pressed:
            self.speed_x += self.ACCELERATION_X

            if self.speed_x > self.MAX_SPEED_X:
                self.speed_x = self.MAX_SPEED_X

        elif self._K_a_pressed:
            self.speed_x -= self.ACCELERATION_X

            if abs(self.speed_x) > self.MAX_SPEED_X:
                self.speed_x = -self.MAX_SPEED_X

        else:
            if self.speed_x > 0:
                self.speed_x -= self.ACCELERATION_X
                self.speed_x = 0 if self.speed_x < 0 else self.speed_x

            if self.speed_x < 0:
                self.speed_x += self.ACCELERATION_X
                self.speed_x = 0 if self.speed_x > 0 else self.speed_x

        self.rect.x += self.speed_x

        # y movement
        if self.is_jumping:
            self.rect.y += self.speed_y  # negative == going up!
            self.speed_y += self.GRAVITY_SPEED  # reduces speed

            print(self.speed_y)
            print(self.rect.y)

            if self.speed_y > 0:
                self.is_falling = True

        if self.rect.y >= 300:  # floor
            self.is_falling = False
            self.is_jumping = False
            self.is_on_floor = True
            self.speed_y = 0
            self.rect.y = 300

        # perform sprite changes
        self.change_sprite()
