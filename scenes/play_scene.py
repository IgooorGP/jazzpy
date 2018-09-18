"""
Module with the scene used to represent
levels of the game.
"""
import pygame

from camera.camera import Camera
from config import SCREEN_HEIGHT, SCREEN_WIDTH
from models.jazz.jazz import Jazz
from scenes.abstract_scene import Scene


class PlayScene(Scene):
    """
    Scene class implementation for play scenes
    of the game.
    """

    def __init__(self, level):
        """ 
        Default constructor of the playscene. Builds a level, creates
        a Jazzi instance and starts the play scene camera.

        Args:
            level (Level): a reference of a level implementation.
        """
        super(PlayScene, self).__init__()
        self.level = level

        # builds the level
        self.level.build()

        # gets jazz
        self.jazz = Jazz(level.jazz_initial_x, level.jazz_initial_y)

        # starts the camera
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT, self.level.total_level_width, self.level.total_level_height)

    def handle_events(self, events):
        """
        Method that handles player's events.

        Args:
            events (list of pygame.event.Event): list of events
        """
        pass

    def update(self):
        """
        Method that calls update on every entity/sprite on the scene in order
        to update its contents positions and states.
        """
        # gets a bool state list of events
        pressed_states = pygame.key.get_pressed()

        # gets bool state of specific keys that matters
        pressed_keys = [
            pressed_states[key]
            for key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_LALT, pygame.K_SPACE)
        ]

        # unpacks states
        up, down, left, right, alt, space = pressed_keys

        # updates jazz
        self.jazz.update(up, down, left, right, alt, space, self.level.platforms)
        self.camera.update(self.jazz)

    def render_on(self, screen):
        """
        Method that blits things on the main screen (surface) of the game.

        Args:
            screen (pygame.Surface): the main game screen to draw surfaces onto.
        """
        # platforms blitting
        for platform in self.level.platforms:
            screen.blit(platform.image, self.camera.apply(platform))

        # jazz blitting
        screen.blit(self.jazz.image, self.camera.apply(self.jazz))
