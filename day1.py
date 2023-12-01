from utils.filereaders import Linereader
from functools import reduce
from re import search

DIGITS_MAP = {'one': 1,
              'two': 2,
              'three': 3,
              'four': 4,
              'five': 5,
              'six': 6,
              'seven': 7,
              'eight': 8,
              'nine': 9}

def day1a(input):
    nums = []
    for line in input:
        num = ""
        num += find_digit(line)
        num += find_digit(line, forward=False)
        nums.append(int(num))
    return sum(nums)


def find_digit(line, forward=1):
    if not forward:
        forward = -1
    for char in line:
        if char.isdigit():
            return char

def day1b(input):
    digits = list(DIGITS_MAP.keys()) + list(str(123456789))
    values = []
    for line in input:
        first = first_digit(line, digits)
        last = last_digit(line, digits)
        values.append(int(first+last))
    return sum(values)


def first_digit(line, digits):
    positions = [line.find(digit) for digit in digits]
    values = []
    for item in positions:
        if item == -1:
            values.append(max(positions) +1)
        else:
            values.append(item)
    first = line[min(values)]
    if first.isdigit():
        return first
    else:
        return str(DIGITS_MAP[str(digits[values.index(min(values))])])

def last_digit(line, digits):
    line = line[::-1]
    digits = [item[::-1] for item in list(DIGITS_MAP.keys())] + list(str(
        123456789))
    positions = [line.find(digit) for digit in digits]
    values = []
    for item in positions:
        if item == -1:
            values.append(max(positions) +1)
        else:
            values.append(item)
    last = line[min(values)]
    print(line, values, last)
    if last.isdigit():
        return last
    else:
        return str(DIGITS_MAP[str(digits[values.index(min(values))])[
                              ::-1]])

data = Linereader("inputs/day1a.txt").content

print(day1b(data))