from typing import Dict, List, Tuple
from pprint import pprint
from itertools import product
import copy
import pdb


def read_data_input(fname: str) -> Tuple[Dict, List, Tuple[int, int]]:
    coords = {}
    folds = []
    x_max = None
    y_max = None
    reading_folds = False
    with open(fname, "r") as f:
        for line in f:
            line = line.strip().strip("\n")
            if not line:
                reading_folds = True
                continue
            if not reading_folds:
                x, y = line.split(",")
                coords[int(x), int(y)] = "#"
            elif reading_folds:
                replace_str = "fold along "
                assert replace_str in line
                line = line.replace(replace_str, "")
                coord, value = line.split("=")
                folds.append((coord, int(value)))
    # pdb.set_trace()
    x_coords = []
    y_coords = []
    for x, y in coords.keys():
        x_coords.append(x)
        y_coords.append(y)
    x_max = max(x_coords) + 1
    y_max = max(y_coords) + 1
    assert x_max is not None
    assert y_max is not None
    dim = (x_max, y_max)
    return (coords, folds, dim)


def perform_a_fold(
    coords: Dict, dim: Tuple[int, int], x: int = None, y: int = None
) -> Dict:
    """
    fold along x or y
    """
    x_max, y_max = dim
    folded_coords = copy.deepcopy(coords)
    if y:
        for i in range(x_max):
            folded_coords[i, y] = "-"
        for i in range(x_max):
            for j in range(y + 1, y_max):
                content = folded_coords.get((i, j), None)
                if content and content != "-" and content != "|":
                    diff = j - y
                    folded_coords[i, y - diff] = folded_coords.pop((i, j))
    if x:
        for j in range(y_max):
            folded_coords[x, j] = "|"
        for i in range(x + 1, x_max):
            for j in range(y_max):
                content = folded_coords.get((i, j), None)
                if content and content != "-" and content != "|":
                    diff = i - x
                    folded_coords[x - diff, j] = folded_coords.pop((i, j))
    return folded_coords


def print_paper(coords: Dict, dim: Tuple[int, int]):
    x_max, y_max = dim
    for j in range(y_max):
        s = ""
        for i in range(x_max):
            content = coords.get((i, j))
            if content is None:
                s += "."
            else:
                s += content
        print(s)


def day13_test_a():
    fname = "days/13/test_input.txt"
    coords, folds, dim = read_data_input(fname)
    pprint(dim)
    pprint(coords)
    pprint(folds)
    print("Initial number of dots#: ", list(coords.values()).count("#"))
    print_paper(coords, dim)
    coord, value = folds[0]
    coords = perform_a_fold(coords, dim, **{coord: value})
    print("number of dots#: ", list(coords.values()).count("#"))
    print_paper(coords, dim)
    coord, value = folds[1]
    coords = perform_a_fold(coords, dim, **{coord: value})
    print("number of dots#: ", list(coords.values()).count("#"))
    print_paper(coords, dim)


def day13_a():
    fname = "days/13/input.txt"
    coords, folds, dim = read_data_input(fname)
    pprint(dim)
    pprint(folds)
    print("Initial number of dots#: ", list(coords.values()).count("#"))
    coord, value = folds[0]
    coords = perform_a_fold(coords, dim, **{coord: value})
    print("number of dots#: ", list(coords.values()).count("#"))
    coord, value = folds[1]
    coords = perform_a_fold(coords, dim, **{coord: value})
    print("number of dots#: ", list(coords.values()).count("#"))


def day13_test_b():
    fname = "days/13/test_input.txt"
    coords, folds, dim = read_data_input(fname)
    pass


def day13_b():
    fname = "days/13/input.txt"
    coords, folds, dim = read_data_input(fname)
    pprint(dim)
    pprint(folds)
    print("Initial number of dots#: ", list(coords.values()).count("#"))
    for coord, value in folds:
        coords = perform_a_fold(coords, dim, **{coord: value})
        print("number of dots#: ", list(coords.values()).count("#"))
    print_paper(coords, dim)


if __name__ == "__main__":
    # day13_test_a()
    # day13_a()
    # day13_tes_b()
    day13_b()
