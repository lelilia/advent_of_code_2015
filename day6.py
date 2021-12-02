""" Advent of Code 2015 day 6 """

import numpy as np

def turn_on(start, stop, grid):
    x0, y0 = start
    x1, y1 = stop
    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            grid[i * 1000 + j] = 1
    return grid


def turn_on_2(start, stop, grid):
    x0, y0 = start
    x1, y1 = stop
    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            grid[i * 1000 + j] += 1
    return grid


def toggle(start, stop, grid):
    x0, y0 = start
    x1, y1 = stop
    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            grid[i * 1000 + j] = (grid[i * 1000 + j] + 1) % 2
    return grid


def toggle_2(start, stop, grid):
    x0, y0 = start
    x1, y1 = stop
    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            grid[i * 1000 + j] += 2
    return grid


def turn_off(start, stop, grid):
    x0, y0 = start
    x1, y1 = stop
    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            grid[i * 1000 + j] = 0
    return grid


def turn_off_2(start, stop, grid):
    x0, y0 = start
    x1, y1 = stop
    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            grid[i * 1000 + j] = max(grid[i * 1000 + j] - 1, 0)
    return grid

if __name__ == "__main__":

    grid = [0] * 1000000
    grid_2 = [0] * 1000000

    with open("input6.txt") as f:
        input = f.readlines()

    for line in input:
        line = line.replace("turn ", "")
        command, start, _, stop = line.split()
        s1, s2 = start.split(",")
        start = (int(s1), int(s2))
        s3, s4 = stop.split(",")
        stop = (int(s3), int(s4))

        if command == "on":
            grid = turn_on(start, stop, grid)
            grid_2 = turn_on_2(start, stop, grid_2)
        elif command == "off":
            grid = turn_off(start, stop, grid)
            grid_2 = turn_off_2(start, stop, grid_2)
        elif command == "toggle":
            grid = toggle(start, stop, grid)
            grid_2 = toggle_2(start, stop, grid_2)

    print("Part1:\t", sum(grid))
    print("Part2:\t", sum(grid_2))
