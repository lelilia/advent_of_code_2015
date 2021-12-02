""" Advent of Code 2015 day 14 """

import numpy as np

INPUT_FILE = "input14.txt"


class Reindeer:
    def __init__(self, name, speed, run_time, rest_time):
        self.name = name
        self.speed = int(speed)
        self.run_time = int(run_time)
        self.rest_time = int(rest_time)
        self.pos = 0
        self.points = 0

    def __repr__(self):
        return self.name + " " + str(self.pos)

    def is_running(self, time):
        return time % (self.run_time + self.rest_time) < self.run_time

    def run(self):
        self.pos += self.speed

    def next_second(self, time):
        if self.is_running(time):
            self.run()

    def get_pos(self):
        return self.pos


with open(INPUT_FILE) as f:
    input = f.readlines()

reindeers = []
for r in input:
    name, _, _, speed, _, _, run_time, _, _, _, _, _, _, rest_time, _ = r.split()
    reindeer = Reindeer(name, speed, run_time, rest_time)
    reindeers.append(reindeer)

for t in range(2503):
    for r in reindeers:
        r.next_second(t)

distances = [r.get_pos() for r in reindeers]
print("Part 1:\t", max(distances))


class Reindeers:
    def __init__(self, input, steps):
        self.reindeers = []
        self.input = input
        self.steps = steps
        self.create_reindeers()
        self.move()
        distances = [r.points for r in self.reindeers]
        print("Part 2:\t", max(distances))

    def create_reindeers(self):
        for r in self.input:
            (
                name,
                _,
                _,
                speed,
                _,
                _,
                run_time,
                _,
                _,
                _,
                _,
                _,
                _,
                rest_time,
                _,
            ) = r.split()
            reindeer = Reindeer(name, speed, run_time, rest_time)
            self.reindeers.append(reindeer)

    def reward_first(self):
        first_pos = 0
        for reindeer in self.reindeers:
            first_pos = max(reindeer.pos, first_pos)
        for reindeer in self.reindeers:
            if reindeer.pos == first_pos:
                reindeer.points += 1

    def move(self):
        for t in range(self.steps):
            for reindeer in self.reindeers:
                reindeer.next_second(t)
            self.reward_first()


r = Reindeers(input, 2503)
