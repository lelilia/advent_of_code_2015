""" Advent of Code 2015 day 9 """
from itertools import permutations

INPUT_FILE = "input9.txt"

directions = {}
cities = []
with open(INPUT_FILE) as f:
    distances = f.readlines()

for distance in distances:
    start, _, stop, _, dist = distance.split()
    directions[(start, stop)] = int(dist)
    if start not in cities:
        cities.append(start)
    if stop not in cities:
        cities.append(stop)


all_possible_combinations = list(permutations(cities, len(cities)))

shortest_distance = 999999999
longest_distance = 0
for combination in all_possible_combinations:

    this_distance = 0
    flag = True
    for i in range(len(combination) - 1):
        if (combination[i], combination[i + 1]) not in directions and (
            combination[i + 1],
            combination[i],
        ) not in directions:
            flag = False
            break
        if (combination[i], combination[i + 1]) in directions:
            this_distance += directions[(combination[i], combination[i + 1])]
        else:
            this_distance += directions[(combination[i + 1], combination[i])]

    if flag:
        longest_distance = max(longest_distance, this_distance)
        shortest_distance = min(shortest_distance, this_distance)

print("Part 1:\t", shortest_distance)
print("Part 2:\t", longest_distance)
