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



class Maze():

    height = None
    width = None
    image = None
    doors = None
    level = 0
    map = []
    tree = []

    def __init__(self, filename = "maze.bmp"):
        self.image = self.convert_color(Image.open(filename))
        self.width = self.image.size[0]
        self.height = self.image.size[1]

        self.genmap(self.image)
        self.doors = self.get_doors()
        return None

    def convert_color(self, image):
        return ImageOps.grayscale(image)

    def genmap(self, image):
        for y in range(self.width):
            for x in range(self.height):
                if image.getpixel((x,y)) < 128:
                    newpixel = Unit(x, y, True, self.level)
                    self.map.append(newpixel)
                else:
                    newpixel = Unit(x, y)
                    self.map.append(newpixel)
        return None

    def get_doors(self):
        doors = []
        for point in self.map:
            if point.y_pos == 0:
                if not point.wall:
                    doors.append(point)
                    continue
            if point.y_pos == self.height-1:
                if not point.wall:
                    doors.append(point)
                    continue
            if point.x_pos == 0:
                if not point.wall:
                    doors.append(point)
                    continue
            if point.x_pos == self.width-1:
                if not point.wall:
                    doors.append(point)
                    continue
        #for door in doors:
        #    print(f'{door.id} :: {door.x_pos}:{door.y_pos} - {door.wall}')
        return doors

    def solve(self):
        actual_point = self.doors[0]
        actual_point.level = 0
        actual_point.visited = True
        while actual_point != self.doors[1]:

            pass




if __name__ == "__main__":
    im = Maze()
    im.solve()