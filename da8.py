from itertools import cycle

from utils.filereaders import Linereader


class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.name} = ({self.left}, {self.right})'


def find_zzz(nodes, instructions):
    instructions = cycle(instructions)
    node = nodes["AAA"]
    steps = 0
    for direction in instructions:
        if node.name == "ZZZ":
            break
        if direction == "L":
            node = nodes[node.leftchar]
        if direction == "R":
            node = nodes[node.rightchar]
        steps += 1
    return steps

def find_zzzb(nodes, instructions):
    instructions = cycle(instructions)
    node = nodes["AAA"]
    steps = 0
    for direction in instructions:
        if node.name == "ZZZ":
            break
        if direction == "L":
            node = nodes[node.leftchar]
        if direction == "R":
            node = nodes[node.rightchar]
        steps += 1
    return steps


def main():
    data = Linereader("inputs/day8.txt").parse()
    instruction = data.pop(0)
    data.pop(0)
    data = [(item[0:3], item[7:10], item[-4:-1]) for item in data]
    nodes = {item[0]: Node(item[0], item[1], item[2]) for item in data}
    print(find_zzz(nodes, instruction))

    from collections import Counter

if __name__ == "__main__":
    main()
