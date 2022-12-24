from collections import defaultdict

class Line:
  def __init__(self, start, end):
    self._startx = int(start[0])
    self._starty = int(start[1])

    self._endx = int(end[0])
    self._endy = int(end[1])

  def __repr__(self):
    return f"({self._startx}, {self._starty})->({self._endx}, {self._endy}), m={self.slope})"

  def __str__(self):
    return f"({self._startx}, {self._starty})->({self._endx}, {self._endy}), m={self.slope})"

  @property
  def slope(self):
    if self._endx == self._startx:
      return None

    if self._endy == self._starty:
      return 0

    return (self._endy - self._starty) / (self._endx - self._startx)

  @property
  def intercept(self):
    return self._starty - (self.slope * self._startx)

  def covered_points(self):
    """Analyzing the data, determined that slope is 1.0, -1.0, 0, or None in
    all datapoints. So we can do this..."""
    leftx, rightx = min(self._startx, self._endx), max(self._startx, self._endx)
    bottomy, topy = min(self._starty, self._endy), max(self._starty, self._endy)
    points = []
    if self.slope == 0:
      for x in range(leftx, rightx + 1):
        points.append((x, self._starty))
    elif self.slope is None:
      for y in range(bottomy, topy + 1):
        points.append((self._startx, y))
    else:
      for x in range(leftx, rightx + 1):
        points.append((x, int(self.slope * x + self.intercept)))
    return points

  @classmethod
  def parse(cls, line_spec):
    starts, ends = line_spec.replace(" ", "").split("->")
    startp = starts.split(",")
    endp = ends.split(",")
    return cls(startp, endp)

with open("input.txt", "r") as f:
  lines = [Line.parse(fileline.strip()) for fileline in f.readlines()]

point_count = defaultdict(int)

for line in lines:
  if line.slope == 0 or line.slope is None:
    for point in line.covered_points():
      point_count[point] += 1

intersects = [count for count in point_count.values() if count >= 2]

print(len(intersects))