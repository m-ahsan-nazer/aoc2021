from typing import List, Dict, Tuple, NewType
from pprint import pprint

TargetArea = NewType("TargetArea", Dict[str, Tuple[int, int]])


def read_data_input(fname: str) -> TargetArea:
    """
    TL TR
    BL BR
    """
    with open(fname, "r") as f:
        line = f.readline()
        line = line.strip().strip("\n")


def day19_test_a():
    fname = "days/19/test_input.txt"
    target_area = read_data_input(fname)


def day19_a():
    fname = "days/19/input.txt"
    target_area = read_data_input(fname)


def day19_test_b():
    fname = "days/19/test_input.txt"
    target_area = read_data_input(fname)


def day19_b():
    fname = "days/19/input.txt"
    target_area = read_data_input(fname)


if __name__ == "__main__":
    day19_test_a()
    # day19_a()
    # day19_test_b()
    # day19_b()
