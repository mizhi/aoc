
with open("input.txt", "r") as f:
    buf = f.readline().strip()

print(buf)

WINDOW_SIZE = 14 # use 4 for problem 1, 14 for problem 2
window = (-WINDOW_SIZE, 0)

def advance_window(window):
    return (window[0] + 1, window[1] + 1)

while window[0] < len(buf):
    if window[0] < 0:
        window = advance_window(window)
        continue

    candidate = buf[window[0]:window[1]]

    if len(candidate) == len(set(candidate)):
        break

    window = advance_window(window)

print(window)
