""" Advent of Code 2015 day 25 """


def find_next(value):
    return (value * 252533) % 33554393


def find_step(row, col):
    row_start = sum(range(row)) + 1
    col_sum = sum(range(col))
    return row_start + col_sum + row * (col - 1)


value = 20151125

steps = find_step(3010, 3019)

for step in range(1, steps):
    value = find_next(value)
print(value)
