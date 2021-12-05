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


def read_table_from_file(
    fname: str, offset: int, whence: int = 0, dim=(5, 5)
) -> Tuple[List[int], int]:
    with open(fname, "r") as f:
        f.seek(offset, whence)
        table = []
        line_num = 0
        line = f.readline()
        while line and line_num < 5:
            line = line.strip().strip("\n").split()
            line = [int(x) for x in line]
            table += line
            line_num += 1
            if line_num == 5:
                break
            line = f.readline()
        # read empty line
        f.readline()
        pos = f.tell()
    return (table, pos)


def read_number_draws_from_file(
    fname: str, offset: int = 0, whence: int = 0
) -> Tuple[List[int], int]:
    with open(fname, "r") as f:
        f.seek(offset, whence)
        line = f.readline().strip("").strip("\n").split(",")
        number_draws = [int(x) for x in line]
        # read empty line
        f.readline()
        pos = f.tell()
    return (number_draws, pos)


def day3_test_a():
    fname = "days/4/test_input.txt"
    number_draws, pos = read_number_draws_from_file(fname)
    tables = []
    end_of_file = False
    while not end_of_file:
        table, pos = read_table_from_file(fname, pos, whence=0)
        tables.append(table)
        with open(fname, "r") as f:
            f.seek(0, 2)
            eof_pos = f.tell()
            if eof_pos == pos:
                end_of_file = True
            f.seek(pos)
    print("day3_test_a")
    print(number_draws)
    print(f"There are {len(tables)} tables")

    table = tables[0]
    row_test = unittest.TestCase()
    row_test.assertEqual(get_table_row(table, 0, (5, 5)), [22, 13, 17, 11, 0])
    row_test.assertEqual(get_table_row(table, 4, (5, 5)), [1, 12, 20, 15, 19])
    col_test = unittest.TestCase()
    col_test.assertEqual(get_table_col(table, 0, (5, 5)), [22, 8, 21, 6, 1])
    col_test.assertEqual(get_table_col(table, 3, (5, 5)), [11, 4, 16, 18, 15])


def day3_a():
    pass


def day3_test_b():
    pass


def day3_b():
    pass


day3_test_a()
