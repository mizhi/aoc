# https://adventofcode.com/2022/day/3

from functools import reduce
import itertools
from string import ascii_letters


class Ruck:
    def __init__(self, contents):
        self.contents = set(contents)

    def __repr__(self):
        return f"{self.contents}"

with open("input.txt", "r") as f:
    rucks = [Ruck(contents.strip()) for contents in f]

def priority(letters):
    if len(letters) == 0:
        return 0
    return ascii_letters.index(letters[0]) + 1

def compute_group_priority(group):
    common_type = reduce(
        lambda accum, ruck: accum & ruck.contents,
        group,
        set(ascii_letters)
    )
    return priority(list(common_type))

def chunkby(iterable, n=1):
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk

groups = [group for group in chunkby(rucks, 3)]

total_priority = reduce(
    lambda accum, group: accum + compute_group_priority(group),
    groups,
    0
)

print(total_priority)
