from __future__ import annotations

from abc import abstractmethod, ABC


class IComposite(ABC):

    def __init__(self, tracking_id: str):
        self._tracking_id = tracking_id

    @abstractmethod
    def find_by_tracking_id(self, tracking_id: str):
        pass

    @abstractmethod
    def __str__(self):
        pass
