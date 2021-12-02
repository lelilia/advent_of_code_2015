""" Advent of Code 2015 day 7 """

with open("input7.txt") as f:
    input = f.readlines()

circuit = {}
# with open("testinput7.txt") as f:
#     input = f.readlines()

for line in input:

    command, target = line.replace("\n", "").split(" -> ")

    if command.isnumeric():
        circuit[target] = int(command)
    else:
        circuit[target] = command

circuit_1 = dict(circuit)
circuit_2 = dict(circuit)

def get_res(circuit, target):


    if type(circuit[target]) == int:
        return circuit[target]
    elif circuit[target].isnumeric():
        circuit[target] = int(circuit[target])
        return circuit[target]
    elif len(circuit[target].split()) == 1:
        circuit[target] = get_res(circuit, circuit[target])
    else:
        command = circuit[target]
        if "AND" in command:
            a, b = command.split(" AND ")
            if a.isnumeric():
                a = int(a)
            else:
                a = get_res(circuit, a)
            if b.isnumeric():
                b = int(b)
            else:
                b = get_res(circuit, b)
            circuit[target] = a & b

        elif "OR" in command:
            a, b = command.split(" OR ")
            circuit[target] = get_res(circuit, a) | get_res(circuit, b)

        elif "NOT" in command:
            a = command.replace("NOT ", "")
            circuit[target] = ~get_res(circuit, a)

        elif "LSHIFT" in command:
            a, value = command.split(" LSHIFT ")
            circuit[target] = get_res(circuit, a) << int(value)

        elif "RSHIFT" in command:
            a, value = command.split(" RSHIFT ")
            circuit[target] = get_res(circuit, a) >> int(value)

        circuit[target] = circuit[target] % 65536
    return circuit[target]

a = get_res(circuit_1, "a")
print("Part1:\t", a)

circuit_2["b"] = a
print("Part 2:\t", get_res(circuit_2, "a"))