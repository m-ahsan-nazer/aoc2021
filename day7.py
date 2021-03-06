from typing import List
from pprint import pprint


def read_input_data(fname: str) -> List[str]:
    input_data = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip().strip("\n").split(",")
            for c in line:
                input_data.append(int(c))
    return input_data


def day7_a():
    fname = "days/7/input.txt"
    positions = read_input_data(fname)
    costs = {}
    num_pos = max(positions)
    for j in range(num_pos):
        costs[j] = 0
        for i, pos_i in enumerate(positions):
            fuel = abs(pos_i - j)
            costs[j] = costs[j] + fuel

    # pprint(sorted(costs.items(), key=lambda item: item[1]))
    pprint(sorted(costs.items(), key=lambda item: item[1])[0])


def day7_b():
    fname = "days/7/input.txt"
    positions = read_input_data(fname)
    costs = {}
    num_pos = max(positions)
    for j in range(num_pos):
        costs[j] = 0
        for i, pos_i in enumerate(positions):
            fuel = sum(range(1, abs(pos_i - j) + 1))
            costs[j] = costs[j] + fuel

    pprint(sorted(costs.items(), key=lambda item: item[1])[0])
    # pprint(sorted(costs.items(), key=lambda item: item[1]))


if __name__ == "__main__":
    # day7_a()
    day7_b()
