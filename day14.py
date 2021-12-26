from typing import Dict, List, Tuple
from pprint import pprint
import copy


def read_input_data(fname: str) -> Dict:
    input_data = {}
    with open(fname, "r") as f:
        for line in f:
            line = line.strip().strip("\n")
            pair, char = line.split("->")
            pair = pair.strip()
            char = char.strip()
            input_data[pair] = char
    return input_data


def get_polymer_template_as_dict(polymer_template: str) -> Dict:
    polymer = {}
    for i in range(len(polymer_template) - 1):
        key = polymer_template[i : i + 2]
        polymer[key] = 1
    return polymer


def count_occurrences(pt: str) -> Dict:
    pt_set = set(pt)
    pt_counts = {}
    for c in pt_set:
        pt_counts[c] = pt.count(c)

    new_pt_counts_items = sorted(
        pt_counts.items(), key=lambda item: item[1], reverse=False
    )
    min_item = new_pt_counts_items[0]
    max_item = new_pt_counts_items[-1]

    return {"min": min_item, "max": max_item}


def insert_char_get_new_polymer(pt: str, input_data: Dict) -> str:
    new_pt = ""
    for i in range(len(pt) - 1):
        insertion_key = input_data.get(pt[i : (i + 2)])
        if insertion_key:
            new_pt = new_pt + (pt[i] + insertion_key)
        else:
            new_pt = new_pt + pt[i]

    new_pt = new_pt + pt[-1]

    return new_pt


def get_new_polymer(polymer: Dict, polymer_map: Dict) -> Dict:
    # new_polymer = copy.deepcopy(polymer)
    new_polymer = {}
    for key in polymer:
        insertion_key = polymer_map.get(key, None)
        left_insertion = key[0] + insertion_key
        if left_insertion in new_polymer:
            new_polymer[left_insertion] += polymer[key]
        else:
            new_polymer[left_insertion] = polymer[key]

        right_insertion = insertion_key + key[1]
        if right_insertion in new_polymer:
            new_polymer[right_insertion] += polymer[key]
        else:
            new_polymer[right_insertion] = polymer[key]

    # only keep non zero polymer chains
    for key, value in list(new_polymer.items()):
        if value == 0:
            new_polymer.pop(key)
    return new_polymer


def print_polymer(polymer: Dict):
    non_zero_polymer = {}
    for key in polymer:
        if polymer[key] > 0:
            non_zero_polymer[key] = polymer[key]
    pprint(non_zero_polymer)


# def insert_char_and_count(pt)


def day14_test_a():
    fname = "days/14/test_input.txt"
    polymer_template = "NNCB"
    input_data = read_input_data(fname)
    pprint(polymer_template)
    pprint(input_data)
    for i in range(10):
        polymer_template = insert_char_get_new_polymer(polymer_template, input_data)
        # pprint(polymer_template)
        # pprint(counts)
    counts = count_occurrences(polymer_template)
    pprint(counts)
    pprint(counts["max"][1] - counts["min"][1])
    print("done")


def day14_a():
    fname = "days/14/input.txt"
    polymer_template = "NBOKHVHOSVKSSBSVVBCS"
    input_data = read_input_data(fname)
    pprint(polymer_template)
    pprint(input_data)
    for i in range(10):
        polymer_template = insert_char_get_new_polymer(polymer_template, input_data)
    # pprint(polymer_template)
    counts = count_occurrences(polymer_template)
    pprint(counts)
    pprint(counts["max"][1] - counts["min"][1])


def day14_test_b():
    fname = "days/14/test_input.txt"
    polymer_template = "NNCB"
    polymer = get_polymer_template_as_dict(polymer_template)
    pprint(polymer)
    polymer_map = read_input_data(fname)
    for i in range(1):
        polymer = get_new_polymer(polymer=polymer, polymer_map=polymer_map)
        # pprint(polymer)
    pprint(polymer)
    # pprint(len(polymer))
    print("sum: ", sum(polymer.values()))
    # counts = dict.fromkeys(polymer_map.values(), 0)
    counts = {}
    # for key in polymer:
    #     first_char = key[1]
    #     counts[first_char] = 0

    print("counts: ", counts)
    for key in polymer:
        # if key[1] in counts:
        #     counts[key[1]] += polymer[key]
        # else:
        #     counts[key[1]] = polymer[key]
        if polymer_map[key] in counts:
            counts[polymer_map[key]] += polymer[key]
        else:
            counts[polymer_map[key]] = polymer[key]
    pprint(counts)


def day14_b():
    fname = "days/14/input.txt"
    polymer_template = "NBOKHVHOSVKSSBSVVBCS"


if __name__ == "__main__":
    # day14_test_a()
    # day14_a()
    day14_test_b()
    # day14_b()
