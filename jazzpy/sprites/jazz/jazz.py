"""
Module with the class representation
of Jazz the Jack Rabbit.
"""
import os

import pygame
from jazzpy.interfaces.observable import ObservableMixin
from jazzpy.settings.general import PROJECT_ROOT_DIR
from jazzpy.settings.jazz import DEFAULT_POSITION_SPRITE
from jazzpy.settings.jazz import FALLING_SPRITE_1
from jazzpy.settings.jazz import JAZZ_DIMENSIONS
from jazzpy.settings.jazz import JAZZ_OBSERVABLE_ID
from jazzpy.settings.jazz import JUMPING_SPRITE_1
from jazzpy.settings.jazz import RUNNING_SPRITES
from jazzpy.settings.jazz import SHOOTING_SPRITE_1
from jazzpy.settings.jazz import WALKING_SPRITE_1
from jazzpy.settings.jazz import WALKING_SPRITE_2
from jazzpy.settings.jazz import WALKING_SPRITE_3
from jazzpy.settings.jazz import WALKING_SPRITE_4
from jazzpy.settings.physics import ACCELERATION_X
from jazzpy.settings.physics import GRAVITY_SPEED
from jazzpy.settings.physics import INITIAL_JUMP_Y_SPEED
from jazzpy.settings.physics import INITIAL_SHOOTING_DELAY
from jazzpy.settings.physics import MAX_SPEED_X
from jazzpy.sprites.misc.bullet import Bullet
from jazzpy.sprites.misc.hud import Hud
from jazzpy.support.spritesheet import SpriteSheet


class Jazz(pygame.sprite.Sprite, ObservableMixin):
    """
    Jazz's class.
    """

    def __init__(self, level_x: int, level_y: int, hud: Hud):
        """
        Default constructor for the Jazz JackRabbit character class.
        """
        # super class init
        super(pygame.sprite.Sprite, self).__init__()
        super(ObservableMixin, self).__init__()

        # loads the sprite_sheet
        self.sprite_sheet = SpriteSheet(
            os.path.join(PROJECT_ROOT_DIR, "jazzpy/sprites/jazz/spritesheets/jazz.png")
        )

        # adds hud as an observer of Jazz's state
        self.add_observer(hud)

        # jazz default position
        self.speed_x, self.speed_y = 0, 0
        self.accerelation_x, self.acceleration_y = 0, 0

        # jazz surface creation from the spritesheet with given width/height
        self.image = self.sprite_sheet.get_image(
            DEFAULT_POSITION_SPRITE, dimensions=JAZZ_DIMENSIONS
        )

        # jazz rectangle creation for collision detection
        self.rect = self.image.get_rect(
            topleft=(level_x, level_y)  # gets width/height of the img but the position is at x, y
        )

        # jazz HAS the bullets now
        self.bullets = pygame.sprite.Group()

        # sprite control
        self.is_running = False
        self.is_jumping = False
        self.is_falling = False
        self.is_on_floor = False
        self.is_shooting = False
        self.direction = "right"
        self.current_running_sprite = 0

        # HUD data
        self.health = 5
        self.current_weapon = "blaster"
        self.lives = 1
        self.player_score = 0

        # shooting delay
        self.oldtime = 0

    def _get_running_sprite(self):
        """
        Alters Jazz's running sprite on every frame to give a
        movement sensation.
        """

        tpl_sprite = RUNNING_SPRITES[self.current_running_sprite]

        self.current_running_sprite += 1
        self.current_running_sprite = (
            0 if self.current_running_sprite > 3 else self.current_running_sprite
        )

        return tpl_sprite

    def _change_sprite(self, dimensions=JAZZ_DIMENSIONS):
        """
        Performs sprite changes based on Jazz's movements.
        """
        if 0 < abs(self.speed_x) < 0.4:
            self.image = self.sprite_sheet.get_image(WALKING_SPRITE_1, dimensions=dimensions)

        if 0.4 <= abs(self.speed_x) < 0.8:
            self.image = self.sprite_sheet.get_image(WALKING_SPRITE_2, dimensions=dimensions)

        if 0.8 <= abs(self.speed_x) < 1.2:
            self.image = self.sprite_sheet.get_image(WALKING_SPRITE_3, dimensions=dimensions)

        if 1.2 <= abs(self.speed_x) < 1.5:
            self.image = self.sprite_sheet.get_image(WALKING_SPRITE_4, dimensions=dimensions)

        if abs(self.speed_x) >= 2:
            # self.image = self.sprite_sheet.get_image(self.RUNNING_SRITE_1)
            self.image = self.sprite_sheet.get_image(
                self._get_running_sprite(), dimensions=dimensions
            )

        if self.speed_x == 0:
            self.image = self.sprite_sheet.get_image(DEFAULT_POSITION_SPRITE, dimensions=dimensions)

        if self.is_jumping:
            self.image = self.sprite_sheet.get_image(JUMPING_SPRITE_1, dimensions=dimensions)

        if self.is_falling:
            self.image = self.sprite_sheet.get_image(FALLING_SPRITE_1, dimensions=dimensions)

        if self.is_shooting and not self.is_falling and not self.is_jumping and not self.is_running:
            self.image = self.sprite_sheet.get_image(SHOOTING_SPRITE_1, dimensions=dimensions)

        # always, in the end, change flip the sprite
        if self.direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)

    def _platform_collision_callback(self, speed_x, speed_y, platform_sprite):
        """
        Changes Jazz state after a platform collision detection.

        rect.right == rect.topright (x)
        rect.left == rect.topleft (x)

        rect.bottom == rect.bottomleft (y)
        rect.top == rect.topleft (y)
        """
        # bottom platform collision
        if speed_x > 0:
            # self.rect.right = platform_sprite.rect.left
            self.rect.right = platform_sprite.rect.left
            self.is_running = False
            self.speed_x = 0

        if speed_x < 0:
            self.rect.left = platform_sprite.rect.right
            self.is_running = False
            self.speed_x = 0

        if speed_y > 0:
            self.rect.bottom = platform_sprite.rect.top
            self.is_on_floor = True
            self.is_jumping = False
            self.is_falling = False
            self.speed_y = 0

        if speed_y < 0:
            # TODO: upon top collision and jumping: remove the jumping sprite
            self.is_jumping = False
            self.rect.top = platform_sprite.rect.bottom
            self.is_falling = True

    def _enemy_collision_callback(self, enemy_sprite):
        """ Changes Jazz state after an enemy collision detection. """
        pass

    def _detect_collision(self, sprite_collision_candidates, candidate_type, is_x_axis):
        """
        Detects collision with other groups of sprites such as platforms,
        enemies, etc. and for executes a collision callback to change
        the state after the collision.

        Args:
            sprite_collision_candidates (list of pygame.sprite.Sprite):
            sprites list to test collision.

            candidate_type (str): type of the candidate to execute a callback
            after the collision. Can be ("platform", "enemy").
        """
        # checks if jazz collides with any member
        collision_sprites = pygame.sprite.spritecollide(
            self, sprite_collision_candidates, dokill=False, collided=pygame.sprite.collide_rect
        )

        for collision_sprite in collision_sprites:
            # same y collision sprite is used for x collision too
            if candidate_type == "platform" and collision_sprite.is_collidable:

                if is_x_axis:
                    self._platform_collision_callback(self.speed_x, 0, collision_sprite)
                else:
                    self._platform_collision_callback(0, self.speed_y, collision_sprite)

        # after all collision callbacks, change the sprite
        self._change_sprite()

    def _move_x_axis(self, left, right):
        """ Handles x-axis movement. """
        # updates x position
        if right:
            self.is_running = True
            self.direction = "right"
            self.speed_x += ACCELERATION_X

            if self.speed_x > MAX_SPEED_X:
                self.speed_x = MAX_SPEED_X

        elif left:
            self.is_running = True
            self.direction = "left"
            self.speed_x -= ACCELERATION_X

            if abs(self.speed_x) > MAX_SPEED_X:
                self.speed_x = -MAX_SPEED_X

        elif not (left or right):
            if self.speed_x > 0:
                self.speed_x -= 2 * ACCELERATION_X
                self.speed_x = 0 if self.speed_x < 0 else self.speed_x

            if self.speed_x < 0:
                self.speed_x += 2 * ACCELERATION_X
                self.speed_x = 0 if self.speed_x > 0 else self.speed_x

            if self.speed_x == 0:
                self.is_running = False

        self.rect.right += self.speed_x

    def _move_y_axis(self, alt):
        """
        Handles y-axis movement.
        Forces jazz to always be falling with a certain speed y which gets
        corrected by collision detection if he's on a platform.
        """
        if alt and self.is_on_floor:
            self.is_jumping = True
            self.speed_y = -INITIAL_JUMP_Y_SPEED  # negative for moving up!

        # updates y position
        if not self.is_on_floor:
            self.speed_y += GRAVITY_SPEED  # reduces speed (adds +)

        self.is_on_floor = False

        if self.speed_y > 1:
            self.is_falling = True

        self.rect.bottom += self.speed_y

    def _change_shooting_state(self, space):
        """ Shoots """
        self.is_shooting = bool(space)

        if self.is_shooting:

            newtime = pygame.time.get_ticks()

            if self.oldtime == 0 or newtime - self.oldtime > INITIAL_SHOOTING_DELAY:

                if newtime - self.oldtime < 1000:
                    if self.direction == "right":
                        bullet = Bullet(
                            self.rect.midright[0], self.rect.midright[1] + 5, self.direction
                        )

                    else:
                        bullet = Bullet(
                            self.rect.midleft[0], self.rect.midleft[1] + 5, self.direction
                        )

                    self.bullets.add(bullet)

                self.oldtime = pygame.time.get_ticks()

    def update(self, pressed_keys, platforms):
        """ Updates jazz's (x, y) positions. """
        left, right, alt, space = pressed_keys

        self._move_x_axis(left, right)
        self._detect_collision(platforms, "platform", is_x_axis=True)

        self._move_y_axis(alt)
        self._detect_collision(platforms, "platform", is_x_axis=False)

        self._change_shooting_state(space)

        # updates the HUD with Jazz's data
        observable_state = {
            "lives": self.lives,
            "world": 1,  # hardcoded for now
            "current_weapon": self.current_weapon,
            "health": self.health,
            "player_score": self.player_score,
        }

        self._notify_observers(observable_state=observable_state, observable_id=JAZZ_OBSERVABLE_ID)
