from Adapter.client_interface import ClientInterface
from Adapter.jpg_image import JpgImage
from Adapter.png_image import PngImage
from Adapter.service import Service


class Adapter(ClientInterface):

    def __init__(self, service: Service):
        self.service = service

    def upload_image_to_service(self, jpg_image: JpgImage):
        self.service.upload_image(PngImage(jpg_image=jpg_image))
