import re

def read_stack_drawing(f):
    lines = []
    while True:
        line = f.readline().strip()
        if line == "":
            break
        lines.append(line)

    return lines

def build_stacks_from_drawing(lines):
    # last line has the stack labels
    stack_names = lines.pop().split()
    stacks = {
        n: []
        for n in stack_names
    }

    # two ways to read stack configuration
    lines = list(reversed(lines))
    for line in lines:
        for i in range(0, len(line), 4):
            stack = i // 4 + 1
            mc = line[i:i+3]
            if "[" in mc:
                stacks[str(stack)].append(line[i:i+3])

    return stacks

MOVE_RE = re.compile(
    "^move\s+(?P<num_crates>\d+)\s+"
    "from\s+(?P<source_stack>\d+)\s+"
    "to\s+(?P<dest_stack>\d+)\s*$"
)
def read_moves(f):
    # moves represented by list of tuples
    # each tuple is (number of creates, source, dest)
    # line is specified as "move 3 from 8 to 9"
    moves = []
    for line in f:
        move_extract = re.match(MOVE_RE, line)
        move = (
            int(move_extract.group("num_crates")),
            move_extract.group("source_stack"),
            move_extract.group("dest_stack")
        )
        moves.append(move)

    return moves

def move_crate(stacks, num, src, dst):
    crates=[]
    for i in range(0, num):
        crates.append(stacks[src].pop())

    for i in range(0, num):
        stacks[dst].append(crates.pop())

def run_moves(moves, stacks):
    for (num, src, dst) in moves:
        move_crate(stacks, num, src, dst)

def pp_stacks(stacks):
    for (k, v) in stacks.items():
        print(k, v)

with open("input.txt", "r") as f:
    stacks = build_stacks_from_drawing(read_stack_drawing(f))
    moves = read_moves(f)


pp_stacks(stacks)
run_moves(moves, stacks)

s = ""
for v in stacks.values():
    s += v[-1][1]

print("---")
pp_stacks(stacks)

print(s)
