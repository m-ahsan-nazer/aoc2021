from os import get_inheritable
from typing import List, Tuple, Dict, NewType
from itertools import product
from pprint import pprint

DataDictType = NewType("DataDictType", Dict[Tuple[int, int], int])
DimType = NewType("DimType", Tuple[int, int])


def read_input_data(fname: str) -> Tuple[DataDictType, DimType]:
    data = {}
    with open(fname, "r") as f:
        i = 0
        for line in f:
            line = line.strip().strip("\n")
            for j, c in enumerate(line):
                data[i, j] = int(c)
            i += 1

        return (data, (i, j + 1))


def get_neighbors(point: DataDictType, area: DataDictType):
    assert len(point) == 1
    neighbors = {}
    (coords, point_height) = point.copy().popitem()
    x, y = coords
    for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        height = area.get((i, j), None)
        if height is not None:
            neighbors[i, j] = height
    return neighbors


def is_lowest_point(point: DataDictType, neighbors: DataDictType) -> bool:
    assert len(point) == 1
    assert len(neighbors) in [2, 3, 4]
    (_, point_height) = point.copy().popitem()
    return point_height < min(list(neighbors.values()))


def day9_test_a():
    fname = "days/9/test_input.txt"
    area, dim = read_input_data(fname)
    print("dimension: ", dim)
    dim_x, dim_y = dim
    low_points = {}
    for i, j in product(range(dim_x), range(dim_y)):
        point = {(i, j): area[i, j]}
        neighbors = get_neighbors(point, area.copy())
        if is_lowest_point(point, neighbors):
            low_points.update(point)

    print(f"There are {len(low_points)} low points")
    risk_levels = sum(low_points.values()) + len(low_points)
    print(f"Sum of risk levels is  {risk_levels} :")
    for point in low_points.items():
        pprint(point)


def day9_a():
    fname = "days/9/input.txt"
    area, dim = read_input_data(fname)
    print("dimension: ", dim)
    dim_x, dim_y = dim
    low_points = {}
    for i, j in product(range(dim_x), range(dim_y)):
        point = {(i, j): area[i, j]}
        neighbors = get_neighbors(point, area.copy())
        if is_lowest_point(point, neighbors):
            low_points.update(point)

    print(f"There are {len(low_points)} low points")
    risk_levels = sum(low_points.values()) + len(low_points)
    print(f"Sum of risk levels is  {risk_levels} :")
    # for point in low_points.items():
    # pprint(point)


def day9_test_b():
    pass


def day9_b():
    pass


# day9_test_a()
day9_a()
