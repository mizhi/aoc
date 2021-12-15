# https://adventofcode.com/2021/day/2

from dataclasses import dataclass

@dataclass
class Position:
  x: int = 0
  depth: int = 0

with open("input.txt", "r") as f:
  program = [x.strip().split() for x in f.readlines()]

sub_pos = Position()
for (command, quantity) in program:
  quantity = int(quantity)
  if command == 'forward':
    sub_pos.x += quantity
  elif command == 'down':
    sub_pos.depth += quantity
  elif command == 'up':
    sub_pos.depth -= quantity

print(sub_pos.depth * sub_pos.x)