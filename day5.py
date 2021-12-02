""" Advent of Code 2015 day 5 """


def at_least_three_vowels(s):
    count = 0
    for v in "aeoui":
        count += s.count(v)
    return count >= 3


def has_double_letter(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return True
    return False


def does_not_contain(s):
    for pair in ["ab", "cd", "pq", "xy"]:
        if pair in s:
            return False
    return True


def is_nice(s):
    return at_least_three_vowels(s) and has_double_letter(s) and does_not_contain(s)


def part1(input):
    count = 0
    for line in input:
        if is_nice(line):
            count += 1
    return count


def contains_double_pairs(s):
    for i in range(len(s)):
        if s[i + 2 :].count(s[i : i + 2]) > 0:
            return True
    return False


def contains_double_with_one_between(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False


def is_nice_two(s):
    return contains_double_with_one_between(s) and contains_double_pairs(s)


def part_2(s):
    count = 0
    for line in input:
        if is_nice_two(line):
            count += 1
    return count


with open("input5.txt") as f:
    input = f.readlines()

# Part 1
assert is_nice("ugknbfddgicrmopn") == True, f"Should be nice"
assert is_nice("aaa") == True
assert is_nice("jchzalrnumimnmhp") == False

print("Part1:\t", part1(input))

# Part 2

assert contains_double_pairs("xyxy") == True
assert contains_double_pairs("aabcdefgaa") == True
assert contains_double_pairs("aaa") == False

assert contains_double_with_one_between("aaa") == True
assert contains_double_with_one_between("efe") == True
assert contains_double_with_one_between("xyx") == True
assert contains_double_with_one_between("aab") == False

assert is_nice_two("qjhvhtzxzqqjkmpb") == True
assert is_nice_two("xxyxx") == True
assert is_nice_two("uurcxstgmygtbstg") == False
assert is_nice_two("ieodomkazucvgmuy") == False

print("Part2:\t", part_2(input))
