from typing import List, Dict, Tuple, NewType
from pprint import pprint

TargetArea = NewType("TargetArea", Dict[str, Tuple[int, int]])


def read_data_input(fname: str) -> TargetArea:
    """
    TL TR
    BL BR
    """
    with open(fname, "r") as f:
        line = f.readline()
        line = line.strip().strip("\n")
        _, target_area = line.split(":")
        target_area = target_area.strip()
        x_vals, y_vals = target_area.split(",")
        x_vals = x_vals.strip().replace("x=", "")
        y_vals = y_vals.strip().replace("y=", "")

        x_min, x_max = x_vals.split("..")
        y_min, y_max = y_vals.split("..")

        x_min = int(x_min)
        x_max = int(x_max)
        y_min = int(y_min)
        y_max = int(y_max)
        return {
            "TL": (x_min, y_max),
            "TR": (x_max, y_max),
            "BL": (x_min, y_min),
            "BR": (x_max, y_min),
        }


def get_vx_min(target_area: TargetArea) -> Tuple[int, int]:
    """
    vx_min affords the largest amount of time in air
    """
    (x_min, _) = target_area.get("TL")
    (x_max, _) = target_area.get("TR")
    t = 0
    vx_min = 0
    x_dist = 0
    over_shoot = False
    while True:
        t += 1
        vx = t
        x_dist = sum(range(vx, -1, -1))
        if x_min <= x_dist <= x_max:
            vx_min = vx
            break
        elif x_dist > x_max:
            over_shoot = True
            break
    # should never over shoot
    assert not over_shoot

    return (x_dist, vx_min)


def get_vx_max(target_area: TargetArea) -> Tuple[int, int]:
    (x_min, _) = target_area.get("TL")
    (x_max, _) = target_area.get("TR")
    vx_max = x_max - 1
    x_dist = sum(range(vx_max, -1, -1))
    return (x_dist, vx_max)


def get_vy_max(target_area: TargetArea) -> Tuple[int, int, int]:
    (_, y_max) = target_area.get("TL")
    (_, y_min) = target_area.get("BL")
    # shooting upwards we always return to y=0 because of symmetry
    # at y=0 vy_max should not overshoot the target area
    vy_max = abs(y_min) - 1
    vy = vy_max
    y_dist = 0
    y = 0
    y_max = 0
    while vy > -vy_max:
        # print(f"vy={vy}, y={y}, y_dist={y_dist}, y_max={y_max}")
        y = y + vy
        y_dist += abs(vy)
        if y > y_max:
            y_max = y
        vy -= 1
    return (y_dist, vy_max, y_max)


def day17_test_a():
    fname = "days/17/test_input.txt"
    target_area = read_data_input(fname)
    pprint(target_area)

    x_dist, vx = get_vx_min(target_area)
    print(f"x_dist={x_dist}, vx={vx}")
    y_dist, vy, y_max = get_vy_max(target_area)
    print(f"y_dist={y_dist}, vy={vy}, y_max={y_max}")


def day17_a():
    fname = "days/17/input.txt"
    target_area = read_data_input(fname)
    pprint(target_area)

    x_dist, vx = get_vx_min(target_area)
    print(f"x_dist={x_dist}, vx={vx}")
    y_dist, vy, y_max = get_vy_max(target_area)
    print(f"y_dist={y_dist}, vy={vy}, y_max={y_max}")


def day17_test_b():
    fname = "days/17/test_input.txt"
    target_area = read_data_input(fname)


def day17_b():
    fname = "days/17/input.txt"
    target_area = read_data_input(fname)


if __name__ == "__main__":
    # day17_test_a()
    day17_a()
    # day17_test_b()
    # day17_b()
