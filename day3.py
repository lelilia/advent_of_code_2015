""" Advent of Code 2015 day 3 """

with open("input3.txt") as f:
    directions = f.read()

houses = {}
houses_2 = {}
houses[(0, 0)] = True
houses_2[(0, 0)] = True
x = y = 0
x_s = y_s = x_r = y_r = 0

for i, direction in enumerate(directions):
    if direction == ">":
        x += 1
        if i % 2 == 0:
            x_s += 1
        else:
            x_r += 1
    elif direction == "<":
        x -= 1
        if i % 2 == 0:
            x_s -= 1
        else:
            x_r -= 1
    elif direction == "^":
        y += 1
        if i % 2 == 0:
            y_s += 1
        else:
            y_r += 1
    else:
        y -= 1
        if i % 2 == 0:
            y_s -= 1
        else:
            y_r -= 1
    houses[(x, y)] = True
    houses_2[(x_s, y_s)] = True
    houses_2[(x_r, y_r)] = True

print("Part1:", len(houses))
print("Part2:", len(houses_2))
