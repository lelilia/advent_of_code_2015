""" Advent of Code 2015 day 20 """

import math

input_number = 33100000


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor


print(list(divisorGenerator(100)))
print(sum(list(divisorGenerator(10))) * 10)

house = 1
while True:
    divisors = list(divisorGenerator(house))
    presents1 = sum(divisors) * 10
    presents2 = 0
    for div in divisors:
        if house // div <= 50:
            presents2 += div * 11
    if presents1 >= input_number:
        print(house)
    if presents2 >= input_number:
        print("Part 2:\t", presents2)
        break

    house += 1
