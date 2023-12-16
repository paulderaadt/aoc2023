import re

from utils.filereaders import Linereader
from enum import Enum
from re import finditer

data = Linereader("inputs/day3a").parse()
line_length = len(data[0])
data = ["..." + line + "..." for line in data]
data.insert(0, (line_length + 6) * ".")
data.append((line_length + 6) * ".")

chars = '#$%&*+-/=@'
numbers = [re.finditer("\d{1,3}", line) for line in data]
total = []
y = 0
for y, matches in enumerate(numbers):
    for num in matches:
        left = num.span()[0] - 1
        right = num.span()[1] + 1
        above = y - 1
        below = y + 1
        if any([char in data[y][left:right] for char in chars]):
            total.append(data[y][left + 1:right - 1])
            continue
        if any([char in data[above][left:right] for char in chars]):
            total.append(data[y][left + 1:right - 1])
            continue
        if any([char in data[below][left:right] for char in chars]):
            total.append(data[y][left + 1:right - 1])
            continue

total = [int(num) for num in total]
print(sum(total))

gears = [re.finditer("\*", line) for line in data]
ratios = 0
for y, matches in enumerate(gears):
    for gear in matches:
        print(gear)
