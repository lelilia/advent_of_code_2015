""" Advent of Code 2015 day 8 """

INPUT_FILE = "input8.txt"

length = 0
with open(INPUT_FILE) as f:
    for s in f:
        length += len(s[:-1])
        length -= len(eval(s))

print("Part 1:\t", length)

length2 = 0
with open(INPUT_FILE) as f:
    for s in f:
        length2 += 2 + s.count('"') + s.count("\\")

print("Part 2:\t", length2)
