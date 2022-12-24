with open("input.txt", "r") as f:
  line = f.readlines()[0]

population = [int(x) for x in line.split(",")]

def next_generation(population):
  new_population = []

  for specimen in population:
    if specimen == 0:
      new_population.append(6)
      new_population.append(8)
    else:
      new_population.append(specimen - 1)

  return new_population


for day in range(0, 80):
  population = next_generation(population)

print(len(population))