""" Advent of Code 2015 day 4 """

import hashlib

input = "bgvyzdsv"


def part_1(input):
    int_add = 0
    while True:
        this_input = input + str(int_add)
        if str(hashlib.md5(this_input.encode()).hexdigest()).startswith("00000"):
            break
        int_add += 1
    print(int_add)


def part_2(input):
    int_add = 0
    while True:
        this_input = input + str(int_add)
        if str(hashlib.md5(this_input.encode()).hexdigest()).startswith("000000"):
            break
        int_add += 1
    print(int_add)


part_1(input)
part_2(input)
