"""
Module with the abstract base class
of all scenes of the game.
"""

from abc import ABC
from abc import abstractmethod


class Scene(ABC):
    """
    Abstract base class for creating scenes
    of the game.
    """

    def __init__(self):
        """
        Default constructor of the scene.
        """
        pass

    @abstractmethod
    def update(self):
        """
        Abstract method to update the scene elements before rendering the new state.
        """
        pass

    @abstractmethod
    def render_on(self, screen):
        """
        Abstract method to render the scene on a screen (pygame.Surface).
        """
        pass

    @abstractmethod
    def handle_events(self, events):
        """
        Abstract method to handle events from the event loop.
        """
        pass
