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


def get_neighbors_not_wall(point: DataDictType, area: DataDictType):
    neighbors = get_neighbors(point, area)
    walls = {}
    for coords in neighbors:
        i, j = coords
        if neighbors[i, j] == 9:
            walls[i, j] = neighbors[i, j]
    for coords in walls:
        neighbors.pop(coords)
    return neighbors


def get_walls(area: DataDictType, dim: Tuple[int, int]):
    walls = {}
    x_dim, y_dim = dim
    for i, j in product(range(x_dim), range(y_dim)):
        if area[i, j] == 9:
            walls[i, j] = 9
    return walls


def get_basin(point: DataDictType, area: DataDictType):
    assert len(point) == 1
    area = area.copy()
    # basin = {}
    # while True:
    #     neighbors = get_neighbors_not_wall(point, area)
    #     if len(neighbors) == 0:
    #         break
    #     for coords in neighbors:
    #         area.pop(coords)
    #     basin.update(neighbors)

    basin = point.copy()
    keep_going = True
    while keep_going:
        basin_before_update = basin.copy()
        for coords in basin_before_update:
            point = {coords: basin.get(coords)}
            neighbors = get_neighbors_not_wall(point, area)
            basin.update(neighbors)
        if len(basin_before_update) == len(basin):
            keep_going = False
    # basin.update(point)
    return basin


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

    all_basins = {}
    for coords in low_points:
        i, j = coords
        point = {(i, j): low_points[i, j]}
        basin = get_basin(point, area.copy())
        all_basins[i, j] = len(basin)
        print("point: ", point)
        print("basin: ", len(basin.values()), basin.values())

    all_basins_values = sorted(list(all_basins.values()), reverse=True)
    print(
        "Sizes of largest 3 basins: ",
        all_basins_values[0] * all_basins_values[1] * all_basins_values[2],
    )
    # point = {(0, 1): 1}
    # basin = get_basin(point, area.copy())
    # print("point: ", point)
    # print("basin: ", basin)


def day9_b():
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
    for point in low_points.items():
        pprint(point)

    all_basins = {}
    for coords in low_points:
        i, j = coords
        point = {(i, j): low_points[i, j]}
        basin = get_basin(point, area.copy())
        all_basins[i, j] = len(basin)

    all_basins_values = sorted(list(all_basins.values()), reverse=True)
    print(
        "Sizes of largest 3 basins: ",
        all_basins_values[0] * all_basins_values[1] * all_basins_values[2],
    )
    pass


# day9_test_a()
# day9_a()
# day9_test_b()
day9_b()
