import time

from Adapter.jpg_image import JpgImage
from Proxy.iservice import IService


class Service(IService):

    def operation(self, image_str: str) -> JpgImage:
        print("Establishing connection with real service")
        time.sleep(0.7)
        print(f"Downloading image '{image_str}' from real service")
        time.sleep(0.8)
        print("Image was downloaded")
        return JpgImage()
