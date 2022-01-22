from dataclasses import dataclass

# https://adventofcode.com/2021/day/3

with open("input.txt", "r") as f:
  readings = [line.strip() for line in f.readlines()]

def count_bits(nums, position):
  counts = {'0': 0, '1': 0}
  for num in nums:
    counts[num[position]] += 1
  return counts

def get_rating(nums, select_func):
  position = 0
  while len(nums) != 1:
    counts = count_bits(nums, position)
    if select_func(counts['0'], counts['1']):
      select_for = '0'
    else:
      select_for = '1'

    nums = [num for num in nums if num[position] == select_for]
    position += 1

  return nums[0]

def get_oxygen_rating(nums):
  return get_rating(nums, select_func=int.__gt__)

def get_co2_rating(nums):
  return get_rating(nums, select_func=int.__le__)

def bitstr_to_int(nums):
  numi = None
  for digit in nums:
    if numi is not None:
      numi <<= 1
    else:
      numi = 0
    if digit == '1':
      numi |= 1
  return numi

test_nums = [
  '00100',
  '11110',
  '10110',
  '10111',
  '10101',
  '01111',
  '00111',
  '11100',
  '10000',
  '11001',
  '00010',
  '01010'
]

o2_rating = bitstr_to_int(get_oxygen_rating(readings))
co2_rating = bitstr_to_int(get_co2_rating(readings))

print(o2_rating * co2_rating)