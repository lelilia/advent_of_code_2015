""" Advent of Code 2015 day 13 """
from itertools import permutations

INPUT_FILE = "input13.txt"

with open(INPUT_FILE) as f:
    preferences = f.readlines()

people = []
happyness = {}

for preference in preferences:
    person_1, _, effect, value, _, _, _, _, _, _, person_2 = preference.split()
    person_2 = person_2[:-1]
    if effect == "gain":
        value = int(value)
    else:
        value = -int(value)
    if person_1 not in people:
        people.append(person_1)
    if person_2 not in people:
        people.append(person_2)
    happyness[(person_1, person_2)] = value

possibilities = list(permutations(people))


max_happyness = -9999999999
for possibility in possibilities:
    this_happiness = 0
    i = 0
    while i < len(people):
        this_happiness += happyness[
            (possibility[i], possibility[(i + 1) % len(people)])
        ]
        this_happiness += happyness[
            (possibility[(i + 1) % len(people)], possibility[i])
        ]
        i += 1
    max_happyness = max(max_happyness, this_happiness)

print("Part 1:\t", max_happyness)


# Part 2
max_happyness = -999999999
for possibility in possibilities:
    this_happyness = 0
    i = 0
    while i < len(people) - 1:
        this_happyness += happyness[
            (possibility[i], possibility[(i + 1) % len(people)])
        ]
        this_happyness += happyness[
            (possibility[(i + 1) % len(people)], possibility[i])
        ]
        i += 1
    max_happyness = max(max_happyness, this_happyness)

print("Part 2:\t", max_happyness)
