# https://adventofcode.com/2022/day/4

from functools import reduce

class Assignment:
    def __init__(self, start, stop):
        self.srange = set(range(start, stop + 1))

    def overlap(self, other):
        if type(other) is not Assignment:
            return False

        return len(self.srange & other.srange) > 0

    def __repr__(self):
        return f"{self.srange}"


def read_assignment_pairs(f):
    for line in f:
        e1, e2 = line.strip().split(",")
        e1 = e1.split("-")
        e2 = e2.split("-")
        e1 = (int(e1[0]), int(e1[1]))
        e2 = (int(e2[0]), int(e2[1]))

        yield (Assignment(*e1), Assignment(*e2))

with open("input.txt", "r") as f:
    assignment_pairs = [
        assignment_pair
        for assignment_pair in read_assignment_pairs(f)
    ]

total_overlap = reduce(
    lambda accum, pair: accum + (1 if pair[0].overlap(pair[1]) else 0),
    assignment_pairs,
    0
)


print(total_overlap)
