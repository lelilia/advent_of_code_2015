""" Advent of Code 2015 day 16 """


class Aunt:
    def __init__(self, index, props):
        self.index = int(index[:-1])
        self.props = props
        self.children = None
        self.cats = None
        self.samoyeds = None
        self.pomeranians = None
        self.akitas = None
        self.vizslas = None
        self.goldfish = None
        self.trees = None
        self.cars = None
        self.perfumes = None
        self.read_props()

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def read_props(self):
        for prop in self.props.split(", "):
            key, value = prop.split(": ")
            self[key] = int(value)

    def check_aunt(self):
        if self.children is not None:
            if self.children != 3:
                return False
        if self.cats is not None:
            if self.cats != 7:
                return False
        if self.samoyeds is not None:
            if self.samoyeds != 2:
                return False
        if self.pomeranians is not None:
            if self.pomeranians != 3:
                return False
        if self.akitas is not None:
            if self.akitas != 0:
                return False
        if self.vizslas is not None:
            if self.vizslas != 0:
                return False
        if self.goldfish is not None:
            if self.goldfish != 5:
                return False
        if self.trees is not None:
            if self.trees != 3:
                return False
        if self.cars is not None:
            if self.cars != 2:
                return False
        if self.perfumes is not None:
            if self.perfumes != 1:
                return False
        return True

    def check_aunt2(self):
        if self.children is not None:
            if self.children != 3:
                return False
        if self.cats is not None:
            if self.cats <= 7:
                return False
        if self.samoyeds is not None:
            if self.samoyeds != 2:
                return False
        if self.pomeranians is not None:
            if self.pomeranians >= 3:
                return False
        if self.akitas is not None:
            if self.akitas != 0:
                return False
        if self.vizslas is not None:
            if self.vizslas != 0:
                return False
        if self.goldfish is not None:
            if self.goldfish >= 5:
                return False
        if self.trees is not None:
            if self.trees <= 3:
                return False
        if self.cars is not None:
            if self.cars != 2:
                return False
        if self.perfumes is not None:
            if self.perfumes != 1:
                return False
        return True


with open("input16.yml") as f:
    input_text = f.readlines()


for line in input_text:
    _, index, *props = line.split()

    aunt = Aunt(index, " ".join(props))
    aunt2 = Aunt(index, " ".join(props))
    if aunt.check_aunt():
        print("Part 1:\t", index[:-1])

    if aunt2.check_aunt2():
        print("Part 2:\t", index[:-1])
