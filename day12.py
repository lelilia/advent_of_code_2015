""" Advent of Code 2015 day 12 """

import json

INPUT_FILE = "input12.json"

with open(INPUT_FILE) as f:
    data = json.load(f)
    # print(data)


def sum_numbers(data, sum=0):
    n_sum = sum
    if type(data) == int:
        return data
    elif type(data) == list:
        for element in data:
            n_sum += sum_numbers(element, sum)
    elif type(data) == dict:
        for key, value in data.items():
            n_sum += sum_numbers(value, sum)
    return n_sum


def sum_numbers_without_red(data, sum=0):
    n_sum = sum
    if type(data) == int:
        return data
    elif type(data) == list:
        for element in data:
            n_sum += sum_numbers_without_red(element, sum)
    elif type(data) == dict:
        if "red" in data.values():
            return 0
        for key, value in data.items():
            n_sum += sum_numbers_without_red(value, sum)
    return n_sum


print("Part 1:\t", sum_numbers(data))
print("Part 2:\t", sum_numbers_without_red(data))

# tests
assert sum_numbers([1, 2, 3], 0) == 6
assert sum_numbers({"a": 2, "b": 4}, 0) == 6
assert sum_numbers([[[3]]], 0) == 3
assert sum_numbers({"a": {"b": 4}, "c": -1}, 0) == 3
assert sum_numbers({"a": [-1, 1]}, 0) == 0

assert sum_numbers_without_red([1, {"c": "red", "b": 2}, 3]) == 4
assert sum_numbers_without_red([1, 2, 3]) == 6
assert sum_numbers_without_red({"d": "red", "e": [1, 2, 3, 4], "f": 5}) == 0
assert sum_numbers_without_red([1, "red", 5]) == 6
