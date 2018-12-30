"""
Module with the Scene manager which is used to handle
Menu Scenes, Play Scenes, etc.
"""
from jazzpy import GAME_SETTINGS
from jazzpy.levels.diamondus.diamondus_level_one import DiamondusLevelOne
from jazzpy.scenes.play_scene import PlayScene


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
            GAME_SETTINGS["folder_settings"]["game_root"]
            + "/sprites/levels/diamondus/diamondus.png",
            GAME_SETTINGS["folder_settings"]["game_root"]
            + "/levels/diamondus/diamondus_level_one.txt",
            GAME_SETTINGS["folder_settings"]["game_root"]
            + "/music/levels/diamondus/marbelara.mp3",
            platforms_width=60,
            platforms_height=60,
        )

        self.current_scene = PlayScene(diamondus_level_one)

    def update_current_scene(self, screen, event_list):
        """
        Updates the current scene based on a list of Pygame events.
        """
        # each scene handles the events of the queue
        self.current_scene.handle_events(event_list)

        # updates elements of the scene
        self.current_scene.update()

        # renders on the screen the updated scene
        self.current_scene.render_on(screen)

    def get_next_scene(self):
        """
        Returns the next scene for the main loop.
        """
        pass

    def get_level_class(self, world_name, stage_level):
        """
        Gets a World class based on the world_name and the stage level.

        Args:
            world_name (str): the world name (lowercased);
            stage_level (int): the world stage [0,...]

        Returns
            (Level): An instance of a world class.
        """
        pass
