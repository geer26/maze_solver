from PIL import Image

class maze():
    image = None
    width = None
    height = None

    def init(self, filename = "maze.bmp"):
        self.image = Image.open(filename)
        self.width = self.image.size(0)
        self.height = self.image.size(1)



def get_image(name = "maze.bmp"):
    im = Image.open(name)

    print(im.format, im.size, im.mode)


if __name__ == "__main__":
    print("Hello world!")
    get_image()