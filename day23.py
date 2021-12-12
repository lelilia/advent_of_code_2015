""" Advent of Code 2015 day 23 """

INPUT_FILE = "input23.txt"

def execute_computer(input_text, register):
    position = 0
    while position < len(input_text):
        command, value, *rest = input_text[position].strip().replace(",", "").split()
        if command == "hlf":
            register[value] //= 2
            position += 1
        elif command == "tpl":
            register[value] *= 3
            position += 1
        elif command == "inc":
            register[value] += 1
            position += 1
        elif command == "jmp":
            if value[0] == "+":
                position += int(value[1:])
            else:
                position -= int(value[1:])
        elif command == "jie":
            if register[value] % 2 == 0:
                if rest[0][0] == "+":
                    position += int(rest[0][1:])
                else:
                    position -= int(rest[0][1:])
            else:
                position += 1
        elif command == "jio":
            if register[value] == 1:
                if rest[0][0] == "+":
                    position += int(rest[0][1:])
                else:
                    position -= int(rest[0][1:])
            else:
                position += 1
    return register["b"]

with open(INPUT_FILE) as f:
    input_text = f.readlines()

print("Part 1:\t", execute_computer(input_text, {"a": 0, "b": 0}))
print("Part 2:\t", execute_computer(input_text, {"a": 1, "b": 0}))
