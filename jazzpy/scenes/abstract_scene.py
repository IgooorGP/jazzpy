"""
Module with the abstract base class
of all scenes of the game.
"""
from abc import ABC
from abc import abstractmethod
from typing import List

import pygame


class Scene(ABC):
    """
    Abstract base class for creating scenes of the game.
    """

    def __init__(self):
        """
        Default constructor for the scenes. Every scene must hold a variable which
        determines whether a quit event has been captured or not.
        """
        self.has_captured_quit_event = False

    @abstractmethod
    def update(self) -> None:
        """
        Abstract method to update the scene elements before rendering the new state.
        """
        pass

    @abstractmethod
    def render(self) -> None:
        """
        Abstract method to render the scene on a screen (pygame.Surface).
        """
        pass

    @abstractmethod
    def _get_pressed_keys(self) -> List[bool]:
        """
        Gets a list of booleans indicating if the desired keys are pressed or not.
        Each scene should implement its own method for different desired keys may
        be wanted.
        """
        pass

    def _get_all_events(self) -> List[pygame.event.EventType]:
        """
        Gets all player events that were captured by pygame on a SINGLE FRAME.
        """
        return pygame.event.get()
