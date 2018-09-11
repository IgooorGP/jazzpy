"""
Module with the scene used to represent
levels of the game.
"""

from scenes.abstract_scene import Scene
from camera.camera import Camera
from models.jazz.jazz import Jazz
from config import SCREEN_HEIGHT, SCREEN_WIDTH


class PlayScene(Scene):
    """
    Scene class implementation for play scenes
    of the game.
    """

    def __init__(self, level):
        super(PlayScene, self).__init__()
        self.level = level
        self.jazz = Jazz(30, 30)
        self.camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT, self.level.total_level_width, self.total_level_height)

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def render_on(self, screen):
        pass
