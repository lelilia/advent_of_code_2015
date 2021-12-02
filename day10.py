""" Advent of code 2015 day 10 """

INPUT = "1113222113"

i = 0
s = INPUT


def one_step(s):
    length = len(s)
    if length == 1:
        return "1" + s
    i = 1
    current_char = s[0]
    new_s = ""
    count = 1
    while i < length:
        if s[i] == current_char:
            count += 1
        else:
            new_s += str(count) + current_char
            current_char = s[i]
            count = 1
        i += 1
    new_s += str(count) + current_char
    return new_s


def n_steps(s, n):
    for _ in range(n):
        s = one_step(s)
    return s


print("Part 1:\t", len(n_steps(INPUT, 40)))
print("Part 2:\t", len(n_steps(INPUT, 50)))
