from typing import List, Dict, Tuple
from pprint import pprint
from itertools import product


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


def print_path(data: Dict, width: int):
    for y in range(width):
        for x in range(width):
            value = data.get((x, y))
            if value is None:
                print("*", end="")
            else:
                print(value, end="")
        print()


class Tree:
    def __init__(
        self, coord: Tuple[int, int], cum_sum: int, data: Dict, width: int
    ) -> None:
        self.coord = coord
        self.cum_sum = cum_sum + data.get(coord)
        self.right = None
        self.down = None


def populate_tree(node: Tree, data: Dict, width: int):
    x, y = node.coord
    if x + 1 == width and y + 1 == width:
        print(node.cum_sum)
        # return
    elif x + 1 < width:
        node.right = Tree((x + 1, y), node.cum_sum, data, width)
        populate_tree(node.right, data, width)
    elif y + 1 < width:
        node.down = Tree((x, y + 1), node.cum_sum, data, width)
        populate_tree(node.down, data, width)


def get_tree(data: Dict, width: int) -> Dict:
    # origin = Tree((0, 0), 0, data, width)
    # origin is special so
    cum_sum = 0
    sum_square = sum(data.values())
    x, y = (0, 0)
    path = {}
    path[x, y] = 0
    while x + 1 < width or y + 1 < width:
        cum_sum_down = 0
        cum_sum_right = 0
        if x + 1 < width:
            right = data.get((x + 1, y))
            cum_sum_right = cum_sum + right
        if y + 1 < width:
            down = data.get((x, y + 1))
            cum_sum_down = cum_sum + down
        if cum_sum_down > cum_sum_right:
            cum_sum = cum_sum_right
            x += 1
        else:
            cum_sum = cum_sum_down
            y += 1
        path[x, y] = cum_sum
    # origin.right = Tree((1, 0), origin.cum_sum, data, width)
    # origin.down = Tree((0, 1), origin.cum_sum, data, width)
    # populate_tree(origin, data, width)
    return path


def day15_test_a():
    fname = "days/15/test_input.txt"
    data, width = read_input_data(fname)
    print_path(data, width)
    tree = get_tree(data, width)
    print(tree)
    print("all done")


def day15_a():
    fname = "days/15/input.txt"
    data = read_input_data(fname)


def day15_test_b():
    fname = "days/15/test_input.txt"
    data = read_input_data(fname)


def day15_b():
    fname = "days/15/input.txt"
    data = read_input_data(fname)


if __name__ == "__main__":
    day15_test_a()
    # day15_a()
    # day15_test_b()
    # day15_b()
