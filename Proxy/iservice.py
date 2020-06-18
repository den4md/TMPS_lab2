from abc import ABC, abstractmethod

from Adapter.jpg_image import JpgImage


class IService(ABC):

    @abstractmethod
    def operation(self, image_str: str) -> JpgImage:
        pass
