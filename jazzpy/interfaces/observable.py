"""
Module with the observable/subject interfaces.
"""
import abc
from typing import Dict


class ObserverMixin:
    # the HUD class
    def __init__(self):
        pass

    @abc.abstractmethod
    def update(self, observable_state: Dict, observable_id: str) -> None:
        """
        Updates the observer based on observable state changes.
        """
        pass


class ObservableMixin:
    # observable sprite such as Jazz
    def __init__(self):
        self._observers = set()

    def add_observer(self, observer: ObserverMixin) -> None:
        """
        Adds a new observer to watch for this class state changes.
        """
        self._observers.add(observer)

    def _notify_observers(self, observable_state: Dict, observable_id: str):
        """
        Notifies all observers of this Observable state change by passing
        an Observable dictionary to the observers.
        """
        for observer in self._observers:
            observer.update(observable_state, observable_id)
