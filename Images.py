from PIL import Image, ImageFilter

class ImageProcessor:
    def __init__(self, file_path):
        self.img = Image.open(file_path)
        self.file_path = file_path

    def get_thumbnail(self, size):
        self.img.thumbnail(size)
        return self.img

    def blur_image(self):
        self.img = self.img.filter(ImageFilter.BLUR)
        return self.img

    def rotate_image(self, degrees):
        self.img = self.img.rotate(degrees)
        return self.img

    def save_image(self, file_path):
        self.img.save(file_path)
