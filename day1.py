""" Advent of code 2015 day 1 """

with open("input1.txt") as f:
    text = f.read()

print( text.count("(") - text.count(")"))

# Part 2
position = 0
level = 0
for char in text:
    position += 1
    if char == "(":
        level += 1
    else:
        level -= 1
        if level < 0:
            break
print(position)