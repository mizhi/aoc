# https://adventofcode.com/2022/day/3

from functools import reduce
from string import ascii_letters


class Ruck:
    def __init__(self, contents):
        mid_point = len(contents) // 2
        self.left = set(contents[:mid_point])
        self.right = set(contents[mid_point:])
        self.shared = self.left & self.right

    def __str__(self):
        return f"left: {self.left}, right: {self.right}, shared: {self.shared}"

    def __repr__(self):
        return f"left: {self.left}, right: {self.right}, shared: {self.shared}"


with open("input.txt", "r") as f:
    rucks = [Ruck(contents.strip()) for contents in f]

def priority(letters):
    if len(letters) == 0:
        return 0
    return ascii_letters.index(letters[0]) + 1

total_priority = reduce(
    lambda total, ruck: total + priority(list(ruck.shared)),
    rucks,
    0
)

print(total_priority)
