import numpy as np
from itertools import combinations

from utils.filereaders import Linereader


class Galaxy:
    def __init__(self, num, y, x):
        self.num = num
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.num} {self.y} {self.x}'


INFLATION_PARAM = 999999


def main():
    data = Linereader("inputs/day11.txt").parse()
    data = [line.replace(".", "0").replace("#", "1") for line in data]
    data = [list(line) for line in data]
    data = np.asarray(data, dtype=int)
    empty_rows = np.where(~data.any(axis=1))[0]
    empty_cols = np.where(~data.any(axis=0))[0]
    # axis 1 is columns
    # axis 0 is rows
    galaxy_y, galaxy_x = np.where(data)
    galaxies = [Galaxy(i + 1, item[0], item[1]) for i, item in enumerate(zip(
        galaxy_y,
        galaxy_x))]

    pairs = combinations(galaxies, 2)
    distances = []
    for pair in pairs:
        first = pair[0]
        second = pair[1]
        unexpanded_distance = abs(first.x - second.x) + abs(first.y - second.y)
        cols_between = np.sum((min(first.x, second.x) < empty_cols)
                              & (max(first.x, second.x) > empty_cols))
        rows_between = np.sum((min(first.y, second.y) < empty_rows)
                              & (max(first.y, second.y) > empty_rows))
        expanded_distance = unexpanded_distance + INFLATION_PARAM * cols_between
        expanded_distance += rows_between * INFLATION_PARAM
        distances.append(expanded_distance)
    print(sum(distances))


if __name__ == "__main__":
    main()
