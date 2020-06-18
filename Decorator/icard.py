from abc import abstractmethod, ABC


class ICard(ABC):

    @abstractmethod
    def __init__(self, color: str):
        self.color = color

    @abstractmethod
    def action(self):
        pass
