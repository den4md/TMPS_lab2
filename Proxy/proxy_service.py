import time

from Adapter.jpg_image import JpgImage
from Proxy.iservice import IService


class ProxyService(IService):

    def operation(self, image_str: str) -> JpgImage:
        print(f"Reading cached image '{image_str}' from disk")
        time.sleep(0.1)
        print("Image downloaded")
        return JpgImage()
