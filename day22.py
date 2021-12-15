""" Advent of Code 2015 day 22 """

BOSS_HITPOINTS = 55
BOSS_DAMAGE = 8
PLAYER_HITPOINTS = 50
PLAYER_MANA = 500

SPELL_BOOK = {
    0: [53, 4, 0, 1, 0, 0],
    1: [73, 2, 2, 1, 0, 0],
    2: [113, 0, 0, 6, 7, 0],
    3: [173, 3, 0, 6, 0, 0],
    4: [229, 0, 0, 5, 0, 101],
}


def find_minimal_cost(part=1):
    minimal_mana_costs = 9999999999999
    q = [
        [
            i,
            BOSS_HITPOINTS,
            BOSS_DAMAGE,
            PLAYER_HITPOINTS,
            PLAYER_MANA,
            {0: 0, 1: 0, 2: 0, 3: 0, 4: 0},
            0,
            [],
        ]
        for i in range(5)
    ]

    while len(q) > 0:
        spell, bh, bd, ph, pm, a_s, tmc, moves = q.pop(0)
        active_spells = a_s.copy()
        if part == 2:
            ph -= 1
            if ph < 0:
                continue
        armor = 0
        # spell effects:
        for key, value in active_spells.items():
            if value == 0:
                continue
            bh -= SPELL_BOOK[key][1]
            ph += SPELL_BOOK[key][2]
            armor += SPELL_BOOK[key][4]
            pm += SPELL_BOOK[key][5]
            active_spells[key] -= 1
        if bh < 1:
            minimal_mana_costs = min(minimal_mana_costs, tmc)
            continue
        if ph < 1:
            continue

        # cast spell
        active_spells[spell] = SPELL_BOOK[spell][3]
        pm -= SPELL_BOOK[spell][0]
        tmc += SPELL_BOOK[spell][0]

        armor = 0
        # spell effects:
        for key, value in active_spells.items():
            if value == 0:
                continue
            bh -= SPELL_BOOK[key][1]
            ph += SPELL_BOOK[key][2]
            armor += SPELL_BOOK[key][4]
            pm += SPELL_BOOK[key][5]
            active_spells[key] -= 1

        if bh < 1:
            minimal_mana_costs = min(minimal_mana_costs, tmc)
            continue

        ph -= bd - armor

        if ph < 1:
            continue

        for s in range(5):
            if SPELL_BOOK[s][0] + tmc > minimal_mana_costs:
                continue
            if SPELL_BOOK[s][0] > pm:
                continue
            if active_spells[s] > 1:
                continue
            q.append([s, bh, bd, ph, pm, active_spells, tmc, moves + [spell]])
    return minimal_mana_costs


print("Part 1:\t", find_minimal_cost(part=1))
print("Part 2:\t", find_minimal_cost(part=2))
