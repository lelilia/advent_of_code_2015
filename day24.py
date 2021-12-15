""" Advent of Code 2015 day 24 """

import numpy as np
from itertools import combinations

INPUT_FILE = "input24.txt"


def read_input(input_file):
    with open(input_file) as f:
        return f.read().strip().split("\n")


def get_target_sum(presents, n):
    return sum(presents) / n


def get_minimal_length_for_n_piles(presents, target_sum):
    min_number_of_presents = len(presents)

    for num_packages in range(1, len(presents)):
        if min_number_of_presents <= num_packages:
            continue
        for combination in combinations(presents, num_packages):
            if sum(combination) == target_sum and min_number_of_presents > len(
                combination
            ):
                min_number_of_presents = len(combination)
    return min_number_of_presents


def get_minimal_entanglement(presents, number_of_presents, target_sum):
    minimal_quantum_entanglement = max(presents) ** number_of_presents

    for combination in combinations(presents, number_of_presents):
        if sum(combination) == target_sum:
            minimal_quantum_entanglement = min(
                minimal_quantum_entanglement, np.prod(combination)
            )
    return minimal_quantum_entanglement


def solve_n_segments(presents, n):
    target_sum = get_target_sum(presents, n)
    number_of_presents = get_minimal_length_for_n_piles(presents, target_sum)
    return get_minimal_entanglement(presents, number_of_presents, target_sum)


if __name__ == "__main__":
    input_data = read_input(INPUT_FILE)

    presents = [int(p) for p in input_data]

    print("Part 1:\t", solve_n_segments(presents, 3))
    print("Part 2:\t", solve_n_segments(presents, 4))
