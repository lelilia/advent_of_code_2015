""" Advent of Code 2015 day 2 """

with open("input2.txt") as f:
    presents = f.readlines()

# Part 1
area = 0
ribbon = 0
for present in presents:
    x, y, z = present.replace("\n", "").split("x")
    x, y, z = int(x), int(y), int(z)
    area += 2 * x * y + 2 * x * z + 2 * y * z
    area += x * y * z / max(x, y, z)
    ribbon += x * y * z
    ribbon += 2 * x + 2 * y + 2 * z - 2 * max(x, y, z)
print(area)

print(ribbon)
