# https://adventofcode.com/2022/day/4

from functools import reduce

def read_pairs(f):
    for line in f:
        e1, e2 = line.strip().split(",")
        e1 = e1.split("-")
        e2 = e2.split("-")
        e1 = (int(e1[0]), int(e1[1]))
        e2 = (int(e2[0]), int(e2[1]))
        yield (e1, e2)

with open("input.txt", "r") as f:
    work_pairs = [work_pair for work_pair in read_pairs(f)]

def complete_overlap(e1, e2):
    return (e1[0] >= e2[0] and e1[1] <= e2[1]) or \
        (e2[0] >= e1[0] and e2[1] <= e1[1])

total_overlap = reduce(
    lambda accum, pair: accum + (1 if complete_overlap(*pair) else 0),
    work_pairs,
    0
)


print(total_overlap)
