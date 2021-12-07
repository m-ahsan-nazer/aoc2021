from typing import NewType, List, Tuple
from pprint import pprint
import unittest


def get_table_row(table: List[int], i: int, dim: Tuple[int, int] = (5, 5)) -> List[int]:
    """
    i: row index
    """
    dim_x, dim_y = dim
    row = table[slice(i * dim_y, i * dim_y + dim_x)]
    return row


def get_table_col(table: List[int], j: int, dim=(5, 5)) -> List[int]:
    """
    j: col index
    """
    dim_x, dim_y = dim
    col = table[slice(j, dim_x * dim_y, dim_x)]
    return col


def read_input_file(fname: str) -> List[str]:
    """
    Removes newline character from each line
    """
    input_data = []
    with open(fname, "r") as f:
        for line in f:
            input_data.append(line.strip("\n"))
    return input_data


def convert_text_to_tail_head(text_line: str) -> List[Tuple[int, int]]:
    tail, head = text_line.split("->")
    tail = tail.split(",")
    head = head.split(",")
    tail = (int(tail[0]), int(tail[1]))
    head = (int(head[0]), int(head[1]))
    return [tail, head]


def convert_tail_head_to_line(
    tail_head: List[Tuple[int, int]]
) -> List[Tuple[int, int]]:
    tail = tail_head[0]
    head = tail_head[-1]
    tail_x, tail_y = tail
    head_x, head_y = head
    rise = head_y - tail_y
    run = head_x - tail_x
    num_line = []
    if rise == 0 and run != 0:
        sign_run = run // abs(run)
        for i in range(tail_x, head_x + sign_run, sign_run):
            num_line.append((i, tail_y))
    elif run == 0 and rise != 0:
        sign_rise = rise // abs(rise)
        for i in range(tail_y, head_y + sign_rise, sign_rise):
            num_line.append((tail_x, i))
    elif rise != 0 and run != 0:
        gradient = rise / run
        sign_run = run // abs(run)
        for i in range(tail_x, head_x + sign_run, sign_run):
            # y = mx + c
            num_line.append((i, (i - tail_x) * gradient + tail_y))
    return num_line


def is_horizontal(line: List[Tuple[int, int]]) -> bool:
    tail_x, tail_y = line[0]
    head_x, head_y = line[-1]
    return tail_x == head_x


def is_vertical(line: List[Tuple[int, int]]) -> bool:
    tail_x, tail_y = line[0]
    head_x, head_y = line[-1]
    return tail_y == head_y


def get_vent_boundaries(dic: dict) -> List[Tuple[int, int]]:
    """
    A---B
    |   |
    D---C
    return: [A, B, C, D]
    """
    x_coords = []
    y_coords = []
    for info in dic:
        tail_head = info["th"]
        tail, head = tail_head
        x, y = tail
        x_coords.append(x)
        y_coords.append(y)
        x, y = head
        x_coords.append(x)
        y_coords.append(y)

    x_min = min(x_coords)
    y_min = min(y_coords)
    x_max = max(x_coords)
    y_max = max(y_coords)
    A = (x_min, y_min)
    B = (x_max, y_min)
    C = (x_max, y_max)
    D = (x_min, y_max)

    return [A, B, C, D]


def get_vent_area(vent_boundaries: List[Tuple[int, int]]) -> List[List[int]]:
    A, B, C, D = vent_boundaries
    x_min, y_min = A
    x_max, y_max = C
    x_len = x_max - x_min
    y_len = y_max - y_min
    vent_area = []
    for j in range(y_max):
        vent_area.append([0 for i in range(x_max)])
    return vent_area


def draw_on_vent_area(vent_area: List[List[int]], line: List[Tuple[int, int]]):
    for point in line:
        x_coord, y_coord = point
        vent_area[int(y_coord) - 1][int(x_coord) - 1] += 1


def day5_test_a():
    fname = "days/5/test_input.txt"
    input_data = read_input_file(fname)
    num_lines_with_info = []
    for text_line in input_data:
        tail_head = convert_text_to_tail_head(text_line)
        num_line = convert_tail_head_to_line(tail_head)
        line_type = None
        if is_horizontal(tail_head):
            line_type = "h"
        elif is_vertical(tail_head):
            line_type = "v"
        info = {"th": tail_head, "nl": num_line, "lt": line_type}
        num_lines_with_info.append(info)

    pprint(num_lines_with_info[4])

    vent_boundaries = get_vent_boundaries(num_lines_with_info)
    vent_area = get_vent_area(vent_boundaries)
    for info in num_lines_with_info:
        if info["lt"] == "h" or info["lt"] == "v":
            draw_on_vent_area(vent_area, info["nl"])

    pprint(vent_area)
    vent_area_flattened = []
    for row in vent_area:
        for point in row:
            vent_area_flattened.append(point)

    count_0 = vent_area_flattened.count(0)
    count_1 = vent_area_flattened.count(1)
    count_all = len(vent_area_flattened)
    print("count 0: ", count_0)
    print("count 1: ", count_1)
    print("count >=2: ", count_all - count_0 - count_1)


def day5_a():
    fname = "days/5/input.txt"
    input_data = read_input_file(fname)
    num_lines_with_info = []
    for text_line in input_data:
        tail_head = convert_text_to_tail_head(text_line)
        num_line = convert_tail_head_to_line(tail_head)
        line_type = None
        if is_horizontal(tail_head):
            line_type = "h"
        elif is_vertical(tail_head):
            line_type = "v"
        info = {"th": tail_head, "nl": num_line, "lt": line_type}
        num_lines_with_info.append(info)

    vent_boundaries = get_vent_boundaries(num_lines_with_info)
    vent_area = get_vent_area(vent_boundaries)
    for info in num_lines_with_info:
        if info["lt"] == "h" or info["lt"] == "v":
            draw_on_vent_area(vent_area, info["nl"])

    # pprint(vent_area)
    vent_area_flattened = []
    for row in vent_area:
        for point in row:
            vent_area_flattened.append(point)

    count_0 = vent_area_flattened.count(0)
    count_1 = vent_area_flattened.count(1)
    count_all = len(vent_area_flattened)
    print("count 0: ", count_0)
    print("count 1: ", count_1)
    print("count >=2: ", count_all - count_0 - count_1)
    pass


def day5_test_b():
    fname = "days/5/test_input.txt"
    input_data = read_input_file(fname)
    num_lines_with_info = []
    for text_line in input_data:
        tail_head = convert_text_to_tail_head(text_line)
        num_line = convert_tail_head_to_line(tail_head)
        line_type = None
        if is_horizontal(tail_head):
            line_type = "h"
        elif is_vertical(tail_head):
            line_type = "v"
        info = {"th": tail_head, "nl": num_line, "lt": line_type}
        num_lines_with_info.append(info)

    pprint(num_lines_with_info[4])

    vent_boundaries = get_vent_boundaries(num_lines_with_info)
    vent_area = get_vent_area(vent_boundaries)
    for info in num_lines_with_info:
        # if info["lt"] == "h" or info["lt"] == "v":
        draw_on_vent_area(vent_area, info["nl"])

    pprint(vent_area)
    vent_area_flattened = []
    for row in vent_area:
        for point in row:
            vent_area_flattened.append(point)

    count_0 = vent_area_flattened.count(0)
    count_1 = vent_area_flattened.count(1)
    count_all = len(vent_area_flattened)
    print("count 0: ", count_0)
    print("count 1: ", count_1)
    print("count >=2: ", count_all - count_0 - count_1)


def day5_b():
    fname = "days/5/input.txt"
    input_data = read_input_file(fname)
    num_lines_with_info = []
    for text_line in input_data:
        tail_head = convert_text_to_tail_head(text_line)
        num_line = convert_tail_head_to_line(tail_head)
        line_type = None
        if is_horizontal(tail_head):
            line_type = "h"
        elif is_vertical(tail_head):
            line_type = "v"
        info = {"th": tail_head, "nl": num_line, "lt": line_type}
        num_lines_with_info.append(info)

    vent_boundaries = get_vent_boundaries(num_lines_with_info)
    vent_area = get_vent_area(vent_boundaries)
    for info in num_lines_with_info:
        draw_on_vent_area(vent_area, info["nl"])

    vent_area_flattened = []
    for row in vent_area:
        for point in row:
            vent_area_flattened.append(point)

    count_0 = vent_area_flattened.count(0)
    count_1 = vent_area_flattened.count(1)
    count_all = len(vent_area_flattened)
    print("count 0: ", count_0)
    print("count 1: ", count_1)
    print("count >=2: ", count_all - count_0 - count_1)


# day5_test_a()
# day5_a()
# day5_test_b()
day5_b()
