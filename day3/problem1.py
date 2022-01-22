from dataclasses import dataclass

# https://adventofcode.com/2021/day/3


@dataclass
class GammaEpsilon:
  gamma = 0
  epsilon = 0

  def __str__(self):
    return f"{self.gamma}, {self.epsilon}"

with open("input.txt", "r") as f:
  readings = [line.strip() for line in f.readlines()]

def compute_values(nums):
  values = None
  for i in range(0, len(nums[0])):
    if values is None:
      values = GammaEpsilon()
    else:
      values.gamma <<= 1
      values.epsilon <<= 1

    counts = {'0': 0, '1': 0}
    for num in nums:
      counts[num[i]] += 1

    if counts['1'] > counts['0']:
      values.gamma |= 1
    else:
      values.epsilon |= 1

  return values

ge = compute_values(readings)

print(ge)
print(ge.gamma * ge.epsilon)
