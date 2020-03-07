from enum import Enum


class Piece(Enum):
    T = [(0, 1), (1, 1), (2, 1), (1, 2)]
    SQUARE = [(0, 0), (0, 1), (1, 0), (1, 1)]
    STICK = [(0, 0), (0, 1), (0, 2), (0, 3)]
    LEFT_L = [(0, 1), (1, 1), (2, 1), (0, 2)]
    RIGHT_L = [(0, 1), (1, 1), (2, 1), (2, 2)]
    LEFT_DOG = [(0, 2), (1, 2), (1, 1), (2, 1)]
    RIGHT_DOG = [(0, 1), (1, 1), (1, 2), (2, 2)]

    def __init__(self, points):
        self.points = points
        height = 0
        width = 0
        for x,y in points:
            if x > width:
                width = x
            if y > height:
                height = y

        self.width = width
        self.height = height

        self.local_frame = [[0] * width] * height
        for x,y in points:
            self.local_frame[y][x] = 1

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

