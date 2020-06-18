from Adapter.png_image import PngImage


class Service:

    @staticmethod
    def upload_image(png_image: PngImage):
        if isinstance(png_image, PngImage):
            print("Image uploaded successful")
        else:
            print("During uploading image the exception was thrown")
