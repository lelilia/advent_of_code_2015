""" Advent of Code 2015 day 22 """

class Spell():
    def __init__(self, cost, damage, healing, turns, armor, new_mana):
        self.cost = cost
        self.damage = damage
        self.healing = healing
        self.turns = turns
        self.armor = armor
        self.new_mana = new_mana

boss_hitpoints = 55
boss_damage = 8

player_hitpoints = 50
player_mana = 500


active_spells = {0: 0, 1: 0, 2: 0, 3: 0, 4:0}

total_mana_costs = 0
minimal_mana_costs = 9999999999999999999999

spell_book = {
    0: [53, 4, 0, 1, 0, 0],
    1: [73, 2, 2, 1, 0, 0],
    2: [113, 0, 0, 6, 7, 0],
    3: [173, 3, 0, 6, 0, 0],
    4: [229, 0, 0, 5, 0, 101]
}

winning_costs = []

q = [[i, boss_hitpoints, boss_damage, player_hitpoints, player_mana, active_spells, total_mana_costs, []] for i in range(5)]

while len(q) > 0:
    spell, bh, bd, ph, pm, a_s, tmc, moves = q.pop(0)
    active_spells = a_s.copy()
    if tmc > minimal_mana_costs:
        continue
    armor = 0
    # spell effects:
    for key, value in active_spells.items():
        if value == 0:
            continue
        bh -= spell_book[key][1]
        ph += spell_book[key][2]
        armor += spell_book[key][4]
        pm += spell_book[key][5]
        active_spells[key] -= 1
    if bh < 1:
        winning_costs.append([tmc, moves, spell])
        minimal_mana_costs = min(minimal_mana_costs, tmc)
        continue
    if ph < 1:
        continue

    # cast spell
    # check if already active
    if active_spells[spell] > 0:
        continue
    # check if spell affordable:
    if spell_book[spell][0] > pm:
        continue
    active_spells[spell] = spell_book[spell][3]
    pm -= spell_book[spell][0]
    tmc += spell_book[spell][0]

    armor = 0
    # spell effects:
    for key, value in active_spells.items():
        if value == 0:
            continue
        bh -= spell_book[key][1]
        ph += spell_book[key][2]
        armor += spell_book[key][4]
        pm += spell_book[key][5]
        active_spells[key] -= 1

    if bh < 1:
        winning_costs.append([tmc, moves + [spell]])
        minimal_mana_costs = min(minimal_mana_costs, tmc)
        continue

    ph -= bd - armor

    if ph < 1:
        continue

    for s in range(5):
        q.append([s, bh, bd, ph, pm, active_spells, tmc, moves + [spell]])

print("Part 1:\t", minimal_mana_costs)



boss_hitpoints = 55
boss_damage = 8

player_hitpoints = 50
player_mana = 500


active_spells = {0: 0, 1: 0, 2: 0, 3: 0, 4:0}

total_mana_costs = 0
minimal_mana_costs = 9999999999999999999999

spell_book = {
    0: [53, 4, 0, 1, 0, 0],
    1: [73, 2, 2, 1, 0, 0],
    2: [113, 0, 0, 6, 7, 0],
    3: [173, 3, 0, 6, 0, 0],
    4: [229, 0, 0, 5, 0, 101]
}

winning_costs = []

q = [[i, boss_hitpoints, boss_damage, player_hitpoints, player_mana, active_spells, total_mana_costs, []] for i in range(5)]

while len(q) > 0:
    spell, bh, bd, ph, pm, a_s, tmc, moves = q.pop(0)
    active_spells = a_s.copy()
    if tmc > minimal_mana_costs:
        continue

    ph -= 1
    if ph < 0:
        continue
    armor = 0
    # spell effects:
    for key, value in active_spells.items():
        if value == 0:
            continue
        bh -= spell_book[key][1]
        ph += spell_book[key][2]
        armor += spell_book[key][4]
        pm += spell_book[key][5]
        active_spells[key] -= 1
    if bh < 1:
        print("YOU WIN", moves + [spell])
        winning_costs.append([tmc, moves, spell])
        minimal_mana_costs = min(minimal_mana_costs, tmc)
        continue
    if ph < 1:
        continue

    # cast spell
    # check if already active
    if active_spells[spell] > 0:
        continue
    # check if spell affordable:
    if spell_book[spell][0] > pm:
        continue
    active_spells[spell] = spell_book[spell][3]
    pm -= spell_book[spell][0]
    tmc += spell_book[spell][0]

    armor = 0
    # spell effects:
    for key, value in active_spells.items():
        if value == 0:
            continue
        bh -= spell_book[key][1]
        ph += spell_book[key][2]
        armor += spell_book[key][4]
        pm += spell_book[key][5]
        active_spells[key] -= 1

    if bh < 1:
        print("YOU WIN", moves + [spell])
        winning_costs.append([tmc, moves + [spell]])
        minimal_mana_costs = min(minimal_mana_costs, tmc)
        continue

    ph -= bd - armor

    if ph < 1:
        continue

    for s in range(5):
        q.append([s, bh, bd, ph, pm, active_spells, tmc, moves + [spell]])

print("Part 2:\t", minimal_mana_costs)