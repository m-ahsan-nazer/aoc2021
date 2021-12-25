from typing import List, Dict, Tuple, NewType
from pprint import pprint
import copy
from itertools import cycle, product


def read_data_input(fname: str) -> Dict:
    floor = {}
    y = 0
    with open(fname, "r") as f:
        for line in f:
            line = line.strip().strip("\n")
            for x, c in enumerate(line):
                floor[x, y] = c
            y += 1
    return (floor, (x + 1, y))


def print_floor(floor: Dict, dim):
    dim_x, dim_y = dim
    for y in range(dim_y):
        for x in range(dim_x):
            print(floor.get((x, y)), end="")
        print()
    print()


def step(floor: Dict, dim) -> Dict:
    dim_x, dim_y = dim
    new_floor_east = copy.deepcopy(floor)
    # east movement
    for y in range(dim_y):
        for x in range(dim_x):
            if floor[(x + 1) % dim_x, y] == "." and floor[x, y] == ">":
                new_floor_east[(x + 1) % dim_x, y] = ">"
                new_floor_east[x, y] = "."

    new_floor = copy.deepcopy(new_floor_east)
    # south movement
    for x in range(dim_x):
        for y in range(dim_y):
            if (
                new_floor_east[x, (y + 1) % dim_y] == "."
                and new_floor_east[x, y] == "v"
            ):
                new_floor[x, (y + 1) % dim_y] = "v"
                new_floor[x, y] = "."
    return new_floor


def day25_test_a():
    fname = "days/25/test_input.txt"
    floor, dim = read_data_input(fname)
    print("dim: ", dim)
    print_floor(floor, dim)
    step_num: int = 0
    while True:
        step_num += 1
        new_floor = step(floor, dim)
        if set(new_floor.items()) - set(floor.items()) == set():
            break
        floor = new_floor
        # print_floor(floor, dim)
    print("ste_num: ", step_num)
    print_floor(floor, dim)


def day25_a():
    fname = "days/25/input.txt"
    floor, dim = read_data_input(fname)
    print("dim: ", dim)
    # print_floor(floor, dim)
    step_num: int = 0
    while True:
        step_num += 1
        new_floor = step(floor, dim)
        if set(new_floor.items()) - set(floor.items()) == set():
            break
        floor = new_floor
        # print_floor(floor, dim)
        print("ste_num: ", step_num)
    print("ste_num: ", step_num)
    # print_floor(floor, dim)


def day25_test_b():
    """ """
    fname = "days/25/test_input.txt"


def day25_b():
    fname = "days/25/input.txt"


if __name__ == "__main__":
    # day25_test_a()
    day25_a()
    # day25_test_b()
    # day25_b()
