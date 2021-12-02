""" Advent of Code 2015 day 11 """


def first_req(s):
    """Password must include one increasing straight of at least three letters"""
    for i in range(len(s) - 2):
        l1, l2, l3 = s[i], s[i + 1], s[i + 2]
        if (
            "a" <= l1
            and "z" >= l3
            and ord(l1) == ord(l2) - 1
            and ord(l1) == ord(l3) - 2
        ):
            return True
    return False


def second_req(s):
    """Password may not contain i o or l"""
    return s.count("o") + s.count("i") + s.count("l") == 0


def third_req(s):
    """Password must contain at least to different, non-overlapping pairs of letters"""
    pair_1 = None
    pair_2 = None
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            if not pair_1:
                pair_1 = s[i]
                i += 1
            if pair_1:
                if pair_1 != s[i]:
                    return True

        i += 1
    return False


def get_next_option(s):
    s = list(s)
    i = len(s) - 1
    while i >= 0:
        if s[i] != "z":
            s[i] = chr(ord(s[i]) + 1)
            break
        if s[i] == "z":
            s[i] = "a"
        i -= 1
    return "".join(s)


def next_password(s):
    while not (first_req(s) and second_req(s) and third_req(s)):
        s = get_next_option(s)
    return s


n_s = next_password("cqjxjnds")
print("Part 1:\t", n_s)
print("Part 2:\t", next_password(get_next_option(n_s)))
# tests

assert first_req("hijklmmn") == True
assert second_req("hijklmmn") == False
assert first_req("abbceffg") == False
assert third_req("abbceffg") == True
assert third_req("abbcegjk") == False
assert next_password("abcdefgh") == "abcdffaa"
assert next_password("ghijklmn") == "ghjaabcc"
