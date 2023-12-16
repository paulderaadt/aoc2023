from math import sqrt, ceil, floor
from functools import reduce

from utils.filereaders import Linereader

data = Linereader("inputs/day6a.txt").parse()
data = [line.split(" ") for line in data]
data = [list(filter(lambda x: x != "", item)) for item in data]


class Race:
    def __init__(self, duration, record):
        self.duration = int(duration)
        self.record = int(record)

    def __repr__(self):
        return f'Duration {self.duration}  Record {self.record}'

    def solve(self):
        '''
        the solution is a limit on quadratic equation in the form of
        (self.record-self.duration) * self.duration > self.record
        -self.duration**2 + self.record*self.duration - self.record = 0
        a = -1
        b = self.duration
        c = =self.record
        abc formulate it to solve
        :return:
        '''
        a = -1
        b = self.duration
        c = -self.record
        x1, x2 = self._abc_solver(a, b, c)
        if x1 * x2 == self.record:
            x2 -= 1
            x1 += 1
        return (x2 - x1) + 1

    def _abc_solver(self, a, b, c):
        x2 = (-b - sqrt(b**2 - 4 * a * c)) / 2 * a
        x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return ceil(x1), floor(x2)


# solution A
races = []
for i in range(1, len(data[0])):
    races.append(Race(data[0][i], data[1][i]))

answers = []
for race in races:
    answers.append(race.solve())

print(reduce(lambda a, b: a * b, answers))

# solution b
data = Linereader("inputs/day6a.txt").parse()
data = [line.split(":") for line in data]
data = [line[1] for line in data]
data = [line.replace(" ", "") for line in data]

race = Race(data[0], data[1])
print(race.solve())
