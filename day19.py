""" Advent of Code 2015 day 19 """

import numpy as np

INPUT_FILE = "input19.txt"


def get_all_new_molecules_for_one_replacement(molecule, atom, new_atom):
    new_molecules = []
    index = 0
    atom_length = len(atom)
    molecule_length = len(molecule)
    while index <= molecule_length - atom_length:
        try:
            index = molecule.index(atom, index)
            new_molecules.append(
                molecule[:index] + new_atom + molecule[index + atom_length :]
            )
            index += 1
        except ValueError as e:
            break
    return new_molecules


def next_step(molecules, replacements):
    new_molecules = set()
    for molecule in list(molecules):
        for rep in replacements:
            new_molecules.update(
                get_all_new_molecules_for_one_replacement(molecule, *rep)
            )
    return new_molecules


def number_of_steps_to_target_molecule(start_molecule, target_molecule, replacements):
    step = 0
    molecules = [start_molecule]
    while target_molecule not in molecules:
        molecules = next_step(molecules, replacements)
        step += 1
        print(step)
    return step


if __name__ == "__main__":
    with open(INPUT_FILE) as f:
        input_text = f.read()

    *replacements, _, molecule = input_text.strip().split("\n")
    replacements = [r.split(" => ") for r in replacements]

    distinct_molecules = set()
    for rep in replacements:
        atom, new_atom = rep
        distinct_molecules.update(
            get_all_new_molecules_for_one_replacement(molecule, atom, new_atom)
        )

    print("Part 1:\t", len(distinct_molecules))

    ## I solved part 2 by hand ...
    # after studying the input I realized that there are 3 terminal elements and that each replacement that can be reached
    # there are some replacements with the atom C but they are not part of the molecule so we don't need to look at them
    # I replaced each non_terminal with X and the three non_terminals with a, b, c
    # each replacement is either X -> XX or X -> XaXc | XaXbXc | XaXbXbXc so my terminals are in a specific order
    # so i don't really have to care about which replacement it is specifically because even if there are multiple
    # possible options the have the same mask and will take the same amount of steps

    # so now i have to code what i did by hand

    modified_input_text = input_text
    for rep in replacements:
        atom, _ = rep
        modified_input_text = modified_input_text.replace(atom, "X")

    *mod_rep, _, mod_mol = modified_input_text.strip().split("\n")
    mod_rep = [r.split(" => ") for r in mod_rep]

    rep_pos = list(set([a for _, a in mod_rep]))

    step_count = 0
    while len(mod_mol) > 1:
        for rep in rep_pos:
            step_count += mod_mol.count(rep)
            mod_mol = mod_mol.replace(rep, "X")
    print("Part 2:\t", step_count)
