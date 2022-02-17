from PIL import Image, ImageOps
import uuid

class Unit():

    x_pos = None
    y_pos = None
    visited = False
    wall = False
    level = None
    id = None
    parent = None

    def __init__(self, xpos = None, ypos = None, wall = False, level = None):
        self.x_pos = xpos
        self.y_pos = ypos
        self.wall = wall
        self.id = uuid.uuid4()
        self.visited = False
        self.level = level
        print(self.id)


class Maze():

    height = None
    width = None
    image = None
    level = 0
    map = []
    tree = []


    def __init__(self, filename = "maze.bmp"):
        self.image = self.convert_color(Image.open(filename))
        self.width = self.image.size[0]
        self.height = self.image.size[1]

    def convert_color(self, image):
        return ImageOps.grayscale(image)

    def genmap(self, image):
        for x in range(self.width):
            for y in range(self.height):
                #print(image.getpixel((x,y)))
                if image.getpixel((x,y)) <= 127:
                    newpixel = Unit(x, x, True, self.level)
                    self.map.append(newpixel)
                if y == self.height-1: print('\n')



if __name__ == "__main__":
    im = Maze()
    im.genmap(im.image)