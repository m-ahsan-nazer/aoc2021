from typing import Dict, List, Tuple
from pprint import pprint


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


def insert_char_get_new_polymer_and_count(
    pt: str, input_data: Dict
) -> Tuple[str, Tuple[str, int]]:
    new_pt = ""
    for i in range(len(pt) - 1):
        insertion_key = input_data.get(pt[i : (i + 2)])
        if insertion_key:
            new_pt = new_pt + (pt[i] + insertion_key)
        else:
            new_pt = new_pt + pt[i]

    new_pt = new_pt + pt[-1]
    new_pt_set = set(new_pt)
    new_pt_counts = {}

    for c in new_pt_set:
        new_pt_counts[c] = new_pt.count(c)

    new_pt_counts_items = sorted(
        new_pt_counts.items(), key=lambda item: item[1], reverse=False
    )
    min_item = new_pt_counts_items[0]
    max_item = new_pt_counts_items[-1]

    return (new_pt, {"min": min_item, "max": max_item})


def day14_test_a():
    fname = "days/14/test_input.txt"
    polymer_template = "NNCB"
    input_data = read_input_data(fname)
    pprint(polymer_template)
    pprint(input_data)
    for i in range(40):
        polymer_template, counts = insert_char_get_new_polymer_and_count(
            polymer_template, input_data
        )
        # pprint(polymer_template)
        # pprint(counts)
    pprint(counts)


def day14_a():
    fname = "days/14/input.txt"
    polymer_template = "NBOKHVHOSVKSSBSVVBCS"
    input_data = read_input_data(fname)
    pprint(polymer_template)
    pprint(input_data)
    for i in range(40):
        polymer_template, counts = insert_char_get_new_polymer_and_count(
            polymer_template, input_data
        )
    # pprint(polymer_template)
    pprint(counts)
    pprint(counts["max"][1] - counts["min"][1])


def day14_test_b():
    fname = "days/14/test_input.txt"
    polymer_template = "NNCB"


def day14_b():
    fname = "days/14/input.txt"
    polymer_template = "NBOKHVHOSVKSSBSVVBCS"


if __name__ == "__main__":
    day14_test_a()
    # day14_a()
    # day14_test_b()
    # day14_b()
