from typing import List, Tuple, Dict, NewType
from itertools import product
from pprint import pprint


def read_input_data(fname: str) -> List[str]:
    input_data = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip().strip("\n")
            input_data.append(line)
    return input_data


def get_brackets():
    o_brackets = "[,{,(,<".split(",")
    c_brackets = "],},),>".split(",")
    return {"o": o_brackets, "c": c_brackets}


def get_mirror(c: str) -> str:
    brackets = get_brackets()
    o_brackets = brackets.get("o")
    c_brackets = brackets.get("c")
    if c in o_brackets:
        ic = o_brackets.index(c)
        c_mirror = c_brackets[ic]
    elif c in c_brackets:
        ic = c_brackets.index(c)
        c_mirror = o_brackets[ic]
    else:
        raise Exception(f"{c} is not an opening or closing bracket")
    return c_mirror


def day10_test_a():
    fname = "days/10/test_input.txt"
    input_data = read_input_data(fname)


def day10_a():
    # fname = "days/10/input.txt"
    pass


def day10_test_b():
    # fname = "days/10/test_input.txt"
    pass


def day10_b():
    # fname = "days/10/input.txt"
    pass


day10_test_a()
# day10_a()
# day10_test_b()
# day10_b()
