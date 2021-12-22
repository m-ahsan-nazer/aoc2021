from typing import List, Dict, Tuple, NewType
from pprint import pprint
import copy
from itertools import cycle, product

RebootSteps = NewType("RebootSteps", Dict[Tuple[int, int, int], int])
CubeDim = NewType("CubeDim", Tuple[int, int, int])


def read_data_input(
    fname: str,
) -> Tuple[List, CubeDim]:
    """
    off x=18..30,y=-20..-8,z=-3..13
    on x=-41..9,y=-7..43,z=-33..15
    """
    reboot_steps = []
    cube_dim = (101, 101, 101)
    with open(fname, "r") as f:
        for line in f:
            line = line.strip().strip("\n")
            on_off, ranges = line.split(" ")
            on_off = on_off.strip()
            if on_off == "on":
                on_off = 1
            elif on_off == "off":
                on_off = 0
            assert on_off in [0, 1]
            x_range, y_range, z_range = ranges.strip().split(",")

            x_l, x_h = x_range.replace("x=", "").split("..")
            x_l = int(x_l)
            x_h = int(x_h)

            y_l, y_h = y_range.replace("y=", "").split("..")
            y_l = int(y_l)
            y_h = int(y_h)

            z_l, z_h = z_range.replace("z=", "").split("..")
            z_l = int(z_l)
            z_h = int(z_h)

            reboot_step = {
                "x": [x_l, x_h],
                "y": [y_l, y_h],
                "z": [z_l, z_h],
                "of": on_off,
            }
            reboot_steps.append(reboot_step)
    return (reboot_steps, cube_dim)


def get_coord_range(coords: Tuple[int, int]) -> List[int]:
    l, h = coords
    return range(l, h + 1, 1)


def turn_on_off(cuboid: Dict, dim: CubeDim, rs: Dict):
    x_coord = rs.get("x")
    y_coord = rs.get("y")
    z_coord = rs.get("z")
    cube_coords = product(
        get_coord_range(x_coord), get_coord_range(y_coord), get_coord_range(z_coord)
    )
    for point in cube_coords:
        # cuboid[point] = rs.get("of")
        if rs.get("of"):
            cuboid[point] = rs.get("of")
        else:
            if cuboid.get(point) is not None:
                cuboid.pop(point)


def day22_test_a():
    fname = "days/22/test_input.txt"
    reboot_steps, cube_dim = read_data_input(fname)
    pprint(reboot_steps)
    # all cubes are off at the start
    cuboid = {}
    for rs in reboot_steps:
        # print("rs: ", rs)
        turn_on_off(cuboid, cube_dim, rs)
    # pprint(cuboid)
    print("on: ", list(cuboid.values()).count(1))
    print("size cuboid", len(cuboid))


def day22_a():
    fname = "days/22/input.txt"
    reboot_steps, cube_dim = read_data_input(fname)
    pprint(reboot_steps)
    # all cubes are off at the start
    cuboid = {}
    for rs in reboot_steps:
        # print("rs: ", rs)
        turn_on_off(cuboid, cube_dim, rs)
    # pprint(cuboid)
    print("on: ", list(cuboid.values()).count(1))
    print("size cuboid", len(cuboid))


def day22_test_b():
    """ """
    fname = "days/22/test_input.txt"
    reboot_steps, cube_dim = read_data_input(fname)
    pprint(reboot_steps)
    # all cubes are off at the start
    cuboid = {}
    for rs in reboot_steps:
        # print("rs: ", rs)
        turn_on_off(cuboid, cube_dim, rs)
    # pprint(cuboid)
    print("on: ", list(cuboid.values()).count(1))
    print("size cuboid", len(cuboid))


def day22_b():
    fname = "days/22/input.txt"


if __name__ == "__main__":
    # day22_test_a()
    # day22_a()
    day22_test_b()
    # day22_b()
