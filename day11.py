from typing import List, Dict
from itertools import product
from pprint import pprint


def read_data_input(fname: str) -> Dict:
    data_input = {}
    with open(fname, "r") as f:
        row = 0
        for line in f:
            line = line.strip().strip("\n")
            for col, num in enumerate(line):
                data_input[row, col] = int(num)
            row += 1
    return data_input


def increment_neighbors(data: Dict, i: int, j: int):
    # for x, y in product((i - 1, i, i + 1), (j - 1, j, j + 1)):
    for x in (i - 1, i, i + 1):
        for y in (j - 1, j, j + 1):
            if (x, y) == (i, j):
                continue
            if x < 0 or x > 9 or y < 0 or y > 9:
                continue
            if data[x, y] != 0 and data[x, y] != 10:
                data[x, y] += 1

    assert len(data) == 100


def step(data: Dict):
    nrows, ncols = (10, 10)
    for i, j in product(range(nrows), range(ncols)):
        data[i, j] += 1
    assert len(data) == 100

    while 10 in list(data.values()):
        for row in range(nrows):
            for col in range(ncols):
                if data[row, col] == 10:
                    data[row, col] = 0
                    increment_neighbors(data, row, col)


def count_flashes(data: Dict) -> int:
    nrows, ncols = (10, 10)
    count = 0
    for i, j in product(range(nrows), range(ncols)):
        if data[i, j] == 0:
            count += 1
    return count


def print_data(data: Dict):
    for i in range(10):
        s = ""
        for j in range(10):
            s += str(data[i, j])
        print(s)


def day11_test_a():
    fname = "days/11/test_input.txt"
    data_input = read_data_input(fname)
    print("initial data")
    print_data(data_input)
    print("len data: ", len(data_input))

    nsteps = 10
    count = 0
    for i in range(nsteps):
        step(data_input)
        count += count_flashes(data_input)
        print(f"After step {i+1} there are {count} flashes")
        print_data(data_input)


def day11_a():
    fname = "days/11/input.txt"
    data_input = read_data_input(fname)
    pass


def day11_test_b():
    fname = "days/11/test_input.txt"
    data_input = read_data_input(fname)
    pass


def day11_b():
    fname = "days/11/input.txt"
    data_input = read_data_input(fname)
    pass


if __name__ == "__main__":
    day11_test_a()
    # day11_a()
    # day11_test_b()
    # day11_b()
