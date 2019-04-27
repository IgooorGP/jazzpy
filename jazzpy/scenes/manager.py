"""
Module with the Scene manager which is used to handle
Menu Scenes, Play Scenes, etc.
"""


class SceneManager:
    """
    Manager for Scene-based classes.
    """

    def __init__(self, initial_scene):
        """
        Initializes the Scene Manager with the first scene to be displayed which could
        be a MenuScene, a PlayScene, etc.
        """
        self.current_scene = initial_scene

    def update_current_scene(self):
        """
        Updates the current scene based on a list of Pygame events.
        """
        # updates elements of the scene
        self.current_scene.update()

        # renders on the screen the updated scene
        self.current_scene.render()

    def current_scene_captured_quit_event(self):
        """
        Method which is called each frame to check if the player wants to
        quit the game. Checked after the update_current_scene method is called.
        """
        return self.current_scene.has_captured_quit_event
