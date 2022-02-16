from PIL import Image, ImageOps

class Maze():

    height = None
    width = None
    image = None
    map = []


    def __init__(self, filename = "maze.bmp"):
        self.image = self.convert_color(Image.open(filename))
        self.width = self.image.size[0]
        self.height = self.image.size[1]

        print(self.image.format, self.image.size, self.image.mode)

    def convert_color(self, image):
        return ImageOps.grayscale(image)

    def genmap(self, image):
        for x in range(self.width):
            for y in range(self.height):
                print(image.getpixel((x,y)))
                if y == self.height-1: print('\n')



def get_image(name = "maze.bmp"):
    im = Image.open(name)

    print(im.format, im.size, im.mode)


if __name__ == "__main__":
    print("Hello world!")
    #get_image()
    im = Maze()
    im.genmap(im.image)