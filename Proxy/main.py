from Adapter.jpg_image import JpgImage
from Proxy.iservice import IService
from Proxy.proxy_service import ProxyService
from Proxy.service import Service


def client(service: IService, image_str: str) -> JpgImage:
    return service.operation(image_str)


def visualize(image_str: str):
    if image_str in cached_images:
        image = client(ProxyService(), image_str)
    else:
        image = client(Service(), image_str)

    print(f'Image "{image}" is visualized\n')


if __name__ == '__main__':
    cached_images = ["1.jpg", "5.jpg"]

    visualize('1.jpg')
    visualize('2.jpg')
