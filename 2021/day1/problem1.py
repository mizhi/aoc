# https://adventofcode.com/2021/day/1

# Count number of measurements that are bigger than the previous one

with open("input.txt", "r") as f:
  depths = [int(x) for x in f.readlines()]

previous = None
num_increase = 0
for depth in depths:
  if previous:
    if depth > previous:
      num_increase += 1
  previous = depth

print(num_increase)