"""
Module with the Scene manager which is used to handle
Menu Scenes, Play Scenes, etc.
"""
from jazzpy.levels.diamondus.diamondus_level_one import DiamondusLevelOne
from jazzpy.scenes.play_scene import PlayScene
from jazzpy.settings import game_options


class SceneManager:
    """
    Manager for Scene-based classes.
    """

    def __init__(self):
        """
        Initializes the Scene Manager with the mocked
        first stage of the game.
        """
        # sets a default scene the first game stage
        diamondus_level_one = DiamondusLevelOne(
            game_options["folder_settings"]["game_root"]
            + "spritesheets/levels/diamondus/diamondus.png",
            game_options["folder_settings"]["game_root"]
            + "levels/diamondus/diamondus_level_one.txt",
            game_options["folder_settings"]["game_root"] + "music/levels/diamondus/diamondus.mp3",
            platforms_width=60,
            platforms_height=60,
        )

        self.current_scene = PlayScene(diamondus_level_one)

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
