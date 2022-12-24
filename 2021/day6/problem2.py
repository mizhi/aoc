from collections import defaultdict

population_counts = defaultdict(lambda: 0)

with open("input.txt", "r") as pf:
  line = pf.readlines()[0]
  population = [int(x) for x in line.split(",")]

for fish in population:
  population_counts[fish] += 1


for day in range(0, 256):
  for i in range(0, 9):
    population_counts[i - 1] = population_counts[i]

  population_counts[8] = population_counts[-1]
  population_counts[6] += population_counts[-1]
  population_counts[-1] = 0

print(population_counts)

print(sum(population_counts.values()))