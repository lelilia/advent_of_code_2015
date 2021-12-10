""" Advent of Code 2015 day 21 """


class Equipment:
    def __init__(self, cost, damage, armor):
        self.cost = cost
        self.damage = damage
        self.armor = armor


class Player:
    def __init__(self, hit_points, damage, armor):
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor


class Game:
    def __init__(self, player_damage=0, player_armor=0):
        self.boss = Player(100, 8, 2)
        self.you = Player(100, player_damage, player_armor)
        self.turn = 1

        self.players = [Player(100, 8, 2), Player(100, player_damage, player_armor)]

    def you_win(self):
        return self.players[1].hit_points > 0

    def play_game(self):
        while not self.game_over():

            self.players[(self.turn + 1) % 2].hit_points -= max(
                self.players[self.turn].damage
                - self.players[(self.turn + 1) % 2].armor,
                1,
            )
            self.turn = (self.turn + 1) % 2

    def game_over(self):
        return self.players[0].hit_points < 1 or self.players[1].hit_points < 1


weapons = [
    Equipment(8, 4, 0),
    Equipment(10, 5, 0),
    Equipment(25, 6, 0),
    Equipment(40, 7, 0),
    Equipment(74, 8, 0),
]

armors = [
    Equipment(13, 0, 1),
    Equipment(31, 0, 2),
    Equipment(53, 0, 3),
    Equipment(75, 0, 4),
    Equipment(102, 0, 5),
    Equipment(0, 0, 0),  # emtpy armor for when you don't buy any
]

rings = [
    Equipment(25, 1, 0),
    Equipment(50, 2, 0),
    Equipment(100, 3, 0),
    Equipment(20, 0, 1),
    Equipment(40, 0, 2),
    Equipment(80, 0, 3),
    Equipment(0, 0, 0),  # empty rings for when you don't by any
    Equipment(0, 0, 0),
]

# i win when the sum of armor and damage >= 10

minimal_winning_cost = 99999999
maximal_losing_cost = 0
for weapon in weapons:
    this_cost = weapon.cost
    for armor in armors:
        for i, ring1 in enumerate(rings):
            for j in range(i + 1, len(rings)):
                ring2 = rings[j]

                this_armor = armor.armor + ring1.armor + ring2.armor
                this_damage = weapon.damage + ring1.damage + ring2.damage
                this_cost = weapon.cost + armor.cost + ring1.cost + ring2.cost
                g = Game(this_damage, this_armor)
                g.play_game()
                if g.you_win():
                    minimal_winning_cost = min(minimal_winning_cost, this_cost)
                else:
                    maximal_losing_cost = max(maximal_losing_cost, this_cost)


print("Part 1:\t", minimal_winning_cost)
print("Part 2:\t", maximal_losing_cost)
