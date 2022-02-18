from PIL import Image, ImageOps
import uuid

class Node():
    x_pos = None
    y_pos = None
    parent = None
    visited = False

    def __init__(self, x_pos, y_pos, parent = None, visited = True):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.parent = parent
        return None

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
    nodes = []
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
        return doors

    def filter_from_points(self, x_pos, y_pos):
        for point in self.map:
            if point.x_pos == x_pos and point.y_pos == y_pos and not point.wall and not point.visited:
                return point
                print(f'POINT: {point.id}')
            return False

    def solve(self):
        actual_point = self.doors[0]
        actual_point.level = 0
        actual_point.visited = True
        while actual_point != self.doors[1]:
            point_south = None
            point_north = None
            point_west = None
            point_east = None
            #get possible directions
            #get accessible (not wall and not visited) pixels nearby - north
            if actual_point.y_pos != 0:
                point_north = self.filter_from_points(actual_point.x_pos, actual_point.y_pos-1)
            #get accessible (not wall and not visited) pixels nearby - south
            if actual_point.y_pos != self.height-1:
                point_south = self.filter_from_points(actual_point.x_pos, actual_point.y_pos+1)
            # get accessible (not wall and not visited) pixels nearby - east
            if actual_point.x_pos != self.width-1:
                point_east = self.filter_from_points(actual_point.x_pos+1, actual_point.y_pos)
            # get accessible (not wall and not visited) pixels nearby - west
            if actual_point.y_pos != 0:
                point_west = self.filter_from_points(actual_point.x_pos-1, actual_point.y_pos)
            print(f'directions: N:{point_north} , E:{point_east} , S:{point_south}, W:{point_west}')

class ToText():
    image = None
    filename = None

    def __init__(self):
        self.filename = input('Input filename to convert:')
        self.image = Image.open(self.filename)
        self.write_to_txt()
        return None

    def write_to_txt(self):
        fname = str(self.filename.split('.')[0]) + '.txt'
        with open(fname, 'w') as f:
            for column in range(self.image.size[0]):
                for row in range(self.image.size[1]):
                    if self.image.getpixel((row, column)) < 128:
                        f.write('#')
                    else:
                        f.write('o')
                f.write('\n')
        return True



if __name__ == "__main__":
    im = ToText()