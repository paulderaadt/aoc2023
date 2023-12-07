from utils.filereaders import Linereader
from enum import Enum

data = Linereader("inputs/day3a").parse()


from re import finditer
class Coordinate:
    def __init__(self, y, x):
        self.x = int(x)
        self.y = int(y)

class Winds(Enum):
    N = Coordinate(-1, 0)
    NW =  Coordinate(-1, -1)
    NE =  Coordinate(-1, 1)
    S =  Coordinate(1, 0)
    SE =  Coordinate(1, 1)
    SW =  Coordinate(1, -1)
    E =  Coordinate(0, -1)
    W =  Coordinate(0, 1)


class Symbol_Coordinate:
    def __init__(self, y, x, symbol):
        self.x = int(x)
        self.y = int(y)
        self.symbol = symbol

    def find_adjecent_numbers(self, data):
        for wind in Winds:
            x = self.x + wind.value.x
            y = self.y + wind.value.y
            if data[y][x].isdigit():
                print(data[y][x], y, x)
                

    def __repr__(self):
        return f"{self.symbol} Y: {self.y} X: {self.x}"


dont = '1234567890.'

symbol_coordinates = []
for y, line in enumerate(data):
    for x, line in enumerate(line):
        if data[y][x] not in dont:
            symbol_coordinates.append(Symbol_Coordinate(y, x, data[y][x]))

for coord in symbol_coordinates:
    print(coord)
    coord.find_adjecent_numbers(data)
    