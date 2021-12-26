from typing import List, Dict, Tuple
from pprint import pprint


def read_input_data(fname: str) -> Tuple[Dict, int]:
    input_data = {}
    with open(fname, "r") as f:
        y = 0
        for line in f:
            line = line.strip().strip("\n")
            for x, c in enumerate(line):
                input_data[x, y] = int(c)
            y += 1
        width = y
    return (input_data, width)


def day16_test_a():
    fname = "days/16/test_input.txt"


def day16_a():
    fname = "days/16/input.txt"
    data = read_input_data(fname)


def day16_test_b():
    fname = "days/16/test_input.txt"
    data = read_input_data(fname)


def day16_b():
    fname = "days/16/input.txt"
    data = read_input_data(fname)


if __name__ == "__main__":
    day16_test_a()
    # day16_a()
    # day16_test_b()
    # day16_b()
