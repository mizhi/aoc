
class Forest:
    def __init__(self, grid):
        self.grid = grid

    @property
    def height(self):
        return len(self.grid)

    @property
    def width(self):
        return len(self.grid[0])

    def left_trees(self, x, y):
        return self.grid[y][:x]

    def right_trees(self, x, y):
        return self.grid[y][x + 1:]

    def up_trees(self, x, y):
        return [self.grid[j][x] for j in range(0, y)]

    def down_trees(self, x, y):
        return [self.grid[j][x] for j in range(y + 1, len(self.grid))]

    def is_visible(self, x, y):
        if x == 0 or x == len(self.grid[0]) - 1 or \
           y == 0 or y == len(self.grid) - 1:
            return True

        # gather heights in 4 cardinal directions
        left_heights = self.left_trees(x, y)
        right_heights = self.right_trees(x, y)
        up_heights = self.up_trees(x, y)
        down_heights = self.down_trees(x, y)

        return grid[y][x] > max(left_heights) or \
            grid[y][x] > max(right_heights) or \
            grid[y][x] > max(up_heights) or \
            grid[y][x] > max(down_heights)

    def scenic_score(self, x, y):
        def count_trees(tree_list):
            for i in range(len(tree_list)):
                if tree_list[i] >= self.grid[y][x]:
                    break
            return i + 1

        # by definition, these will always be 0
        if x == 0 or x == len(self.grid[0]) - 1 or \
           y == 0 or y == len(self.grid) - 1:
            return 0

        # get the heights so that closer trees appear
        # earlier
        left_heights = list(reversed(self.left_trees(x, y)))
        right_heights = self.right_trees(x, y)
        up_heights = list(reversed(self.up_trees(x, y)))
        down_heights = self.down_trees(x, y)

        return count_trees(left_heights) * \
            count_trees(right_heights) * \
            count_trees(up_heights) * \
            count_trees(down_heights)




grid = []
with open("input.txt", "r") as f:
    for line in f:
        grid.append(list(int(x) for x in line.strip()))

forest = Forest(grid)

# For problem 1, do a brute force computation and compute a visibility grid
visibility = [
    [forest.is_visible(x, y) for x in range(forest.width)]
    for y in range(forest.height)
]

print(sum(row.count(True) for row in visibility))

# Problem 2 is a similar strategy. Compute scenic scores
# for all trees.

scenic_scores = [
    [forest.scenic_score(x, y) for x in range(forest.width)]
    for y in range(forest.height)
]

max_score = 0
for row in scenic_scores:
    for score in row:
        max_score = max(score, max_score)

print(max_score)
