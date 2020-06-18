from Adapter.adapter import Adapter
from Adapter.jpg_image import JpgImage
from Adapter.service import Service

if __name__ == '__main__':
    jpg = JpgImage()

    print("--Uploading a jpg to service--")
    service = Service()
    service.upload_image(jpg)

    print("--Uploading a jpg to service with help of adapter--")
    adapter = Adapter(service=service)
    adapter.upload_image_to_service(jpg_image=jpg)
