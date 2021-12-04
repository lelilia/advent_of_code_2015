""" Advent of Code 2015 day 15 """
import numpy as np

a = np.array([-1, -2, 6, 3])
b = np.array([2, 3, -2, -1])

ARRAY = [
    np.array([3, 0, 0, -3, 2]),
    np.array([-3, 3, 0, 0, 9]),
    np.array([-1, 0, 4, 0, 1]),
    np.array([0, 0, -2, 2, 8]),
]
print(np.add(a, b))


def get_properties(ingredients, quantity):
    # if len(ingredients) != len(quantity):
    #     return []
    # if sum(quantity) != 100:
    #     return

    values = []
    for i in range(len(quantity)):
        values.append(multiply_ingredients(ingredients[i], quantity[i]))
    prop = sum(values)
    if np.all(prop > 0):
        return [np.prod(prop[:-1]), prop[-1]]
    return [0, 0]


def multiply_ingredients(ingredient, quantity):
    return np.array([a_i * quantity for a_i in ingredient])


def try_out_mix():
    max_prop = 0
    max_prop2 = 0
    for i in range(101):
        # max_prop = max(max_prop, get_properties([a, b], [i, 100-i]))
        for j in range(101 - i):
            for k in range(101 - i - j):
                props, cals = get_properties(ARRAY, [i, j, k, 100 - i - j - k])
                max_prop = max(max_prop, props)
                if cals == 500:
                    max_prop2 = max(max_prop2, props)

    print("Part 1:\t", max_prop)
    print("Part 2:\t", max_prop2)


try_out_mix()
