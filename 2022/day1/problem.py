# https://adventofcode.com/2022/day/1

def read_elfpack(f):
    elfpack = []
    for line in f:
        try:
            item = int(line.strip())
            elfpack.append(item)
        except ValueError as e:
            yield elfpack
            elfpack = []

    if len(elfpack) > 0:
        yield elfpack

def read_elfpacks(f):
    return [elfpack for elfpack in read_elfpack(f)]

with open("input.txt", "r") as f:
    elfpacks = read_elfpacks(f)

def sum_packs(packs):
    sums = []
    for pack in packs:
        sums.append(sum(pack))
    return sums

# problem 1
pack_sums = list(reversed(sorted(sum_packs(elfpacks))))
print(pack_sums[0])

# problem 2
print(sum(pack_sums[:3]))
