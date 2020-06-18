from abc import ABC, abstractmethod

from Adapter.jpg_image import JpgImage


class ClientInterface(ABC):

    @abstractmethod
    def upload_image_to_service(self, jpg_image: JpgImage):
        pass
