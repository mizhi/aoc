# https://adventofcode.com/2021/day/1

# Count number of windows
WINDOW_SIZE=3

with open("input.txt", "r") as f:
  depths = [int(x) for x in f.readlines()]

previous = None
num_increase = 0
for i in range(0, len(depths) - WINDOW_SIZE+1):
  window = sum(depths[i:i + WINDOW_SIZE])
  if previous:
    if window > previous:
      num_increase += 1
  previous = window

print(num_increase)
