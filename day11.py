from typing import List


def read_data_input(fname):
    data_input = []
    with open(fname, "r") as f:
        data_input = f.readlines()

    return data_input


def day11_test_a():
    fname = "days/11/test_input.txt"
    data_input = read_data_input(fname)
    pass


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
