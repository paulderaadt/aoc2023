from utils.filereaders import Linereader
import numpy as np


def solve_1a(nums, total):
    if any(nums):
        total += nums[-1]
        return solve_1a(np.diff(nums), total)
    else:
        return total


def main():
    data = Linereader("inputs/day9a.txt").parse()
    data = [item.split() for item in data]
    data = [np.array(item, dtype=np.int64) for item in data]
    ans = []
    for line in data:
        ans.append(solve_1a(line, 0))
    print(sum(ans))
    ans = []
    for line in data:
        ans.append(solve_1a(line[::-1], 0))
    print(sum(ans))


if __name__ == "__main__":
    main()

