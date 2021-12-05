""" Advent of Code 2015 day 17 """
count = 0
min_number = 1000
count2 = 0


def subset_sum(containers, target, partial=[]):
    global count, min_number, count2
    s = sum(partial)
    if s == target:
        min_number = min(len(partial), min_number)
        count += 1
        if len(partial) == 4:
            count2 += 1
    if s >= target:
        return
    for i in range(len(containers)):
        n = containers[i]
        remaining = containers[i + 1 :]
        subset_sum(remaining, target, partial + [n])


containers = [20, 15, 10, 5, 5]

target = 25

containers = [
    50,
    44,
    11,
    49,
    42,
    46,
    18,
    32,
    26,
    40,
    21,
    7,
    18,
    43,
    10,
    47,
    36,
    24,
    22,
    40,
]
target = 150

print(subset_sum(containers, target))
print(count)
print(min_number)
print("Part 2:\t", count2)
