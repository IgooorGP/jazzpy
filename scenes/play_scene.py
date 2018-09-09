"""
Module with the scene used to represent
levels of the game.
"""

from scenes.abstract_scene import Scene


class PlayScene(Scene):
    """
    Scene class implementation for play scenes
    of the game.
    """

    def __init__(self):
        super(PlayScene, self).__init__()

    def handle_events(self, events):
        pass

    def update(self):
        pass

    def render_on(self, screen):
        pass
