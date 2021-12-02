from pprint import pprint
from typing import Tuple


def readInput(fname):
    lines = []
    with open(fname, "r") as f:
        for line in f:
            lines.append(line)
    return lines


def diff(array):
    array_diff = []
    for i in range(1, len(array)):
        array_diff.append(array[i] - array[i - 1])
    return array_diff


def instructionToCoord(instruction: str) -> Tuple[int, int]:
    dir, step_size = instruction.split(" ")
    step_size = int(step_size)
    if dir == "forward":
        return (step_size, 0)
    elif dir == "up":
        return (0, -step_size)
    elif dir == "down":
        return (0, step_size)


def cumSum(values):
    return


def test():
    day2_test_input = """
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
        """
    moves = []
    for line in day2_test_input.strip().split("\n"):
        line = line.strip()
        moves.append(instructionToCoord(line))

    x_moves, y_moves = zip(*moves)
    x_coords = [sum(x_moves[slice(0, i + 1)]) for i in range(len(x_moves))]
    y_coords = [sum(y_moves[slice(0, i + 1)]) for i in range(len(y_moves))]
    coords = list(zip(x_coords, y_coords))

    print(f"mutiplying final position {coords[-1][0]*coords[-1][1]}")


def day2():
    day2_input = readInput("days/2/input.txt")

    moves = []
    for line in day2_input:
        line = line.strip()
        moves.append(instructionToCoord(line))

    x_moves, y_moves = zip(*moves)
    x_coords = [sum(x_moves[slice(0, i + 1)]) for i in range(len(x_moves))]
    y_coords = [sum(y_moves[slice(0, i + 1)]) for i in range(len(y_moves))]
    coords = list(zip(x_coords, y_coords))

    print(f"mutiplying final position {coords[-1][0]*coords[-1][1]}")


# test()
day2()
