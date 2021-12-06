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


def check_for_bingos(table: List[int], numbers: List[int], dim_table=(5, 5)):
    dim_x, dim_y = dim_table
    bingos = {"rows": [], "cols": []}
    for i in range(dim_x):
        row = get_table_row(table, i, dim_table)
        if set(numbers).issuperset(row):
            bingos["rows"].append(i)

    for j in range(dim_y):
        col = get_table_col(table, j, dim_table)
        if set(numbers).issuperset(col):
            bingos["cols"].append(j)
    unmarked_numbers = table.copy()
    for num in numbers:
        count = unmarked_numbers.count(num)
        for i in range(count):
            unmarked_numbers.remove(num)

    score = 0
    if bingos["rows"] or bingos["cols"]:
        score = numbers[-1] * sum(unmarked_numbers)
    bingos["score"] = score

    return bingos


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


def day4_test_a():
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
    print("day4_test_a")
    print(number_draws)
    print(f"There are {len(tables)} tables")

    table = tables[0]
    row_test = unittest.TestCase()
    row_test.assertEqual(get_table_row(table, 0, (5, 5)), [22, 13, 17, 11, 0])
    row_test.assertEqual(get_table_row(table, 4, (5, 5)), [1, 12, 20, 15, 19])
    col_test = unittest.TestCase()
    col_test.assertEqual(get_table_col(table, 0, (5, 5)), [22, 8, 21, 6, 1])
    col_test.assertEqual(get_table_col(table, 3, (5, 5)), [11, 4, 16, 18, 15])

    for num_i, number in enumerate(number_draws):
        bingo_boards = []
        for tab_i, table in enumerate(tables):
            numbers = number_draws[slice(0, num_i + 1)]
            bingos = check_for_bingos(table, numbers, (5, 5))
            if bingos["rows"] or bingos["cols"]:
                bingo_boards.append((bingos["score"], tab_i))
        if bingo_boards:
            break
    print("Checking for winning boards")
    for bingo_board in bingo_boards:
        print(bingo_board)


def day4_a():
    fname = "days/4/input.txt"
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
    print("day4_a")
    print(number_draws)
    print(f"There are {len(tables)} tables")

    for num_i, number in enumerate(number_draws):
        bingo_boards = []
        for tab_i, table in enumerate(tables):
            numbers = number_draws[slice(0, num_i + 1)]
            bingos = check_for_bingos(table, numbers, (5, 5))
            if bingos["rows"] or bingos["cols"]:
                bingo_boards.append((bingos["score"], tab_i))
        if bingo_boards:
            break
    print("Checking for winning boards")
    for bingo_board in bingo_boards:
        print(bingo_board)


def day4_test_b():
    fname = "days/4/test_b_input.txt"
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
    print("day4_test_b")
    print(number_draws)
    print(f"There are {len(tables)} tables")

    table = tables[0]
    row_test = unittest.TestCase()
    row_test.assertEqual(get_table_row(table, 0, (5, 5)), [22, 13, 17, 11, 0])
    row_test.assertEqual(get_table_row(table, 4, (5, 5)), [1, 12, 20, 15, 19])
    col_test = unittest.TestCase()
    col_test.assertEqual(get_table_col(table, 0, (5, 5)), [22, 8, 21, 6, 1])
    col_test.assertEqual(get_table_col(table, 3, (5, 5)), [11, 4, 16, 18, 15])

    bingo_boards = []
    winning_boards = []
    winning_boards_details = []
    for num_i, number in enumerate(number_draws):
        for tab_i, table in enumerate(tables):
            numbers = number_draws[slice(0, num_i + 1)]
            bingos = check_for_bingos(table, numbers, (5, 5))
            if bingos["rows"] or bingos["cols"]:
                bingo_boards.append((bingos["score"], tab_i, num_i, number))
                if tab_i not in winning_boards:
                    winning_boards.append(tab_i)
                    winning_boards_details.append(
                        (bingos["score"], tab_i, num_i, number)
                    )
    print("Checking for winning boards")
    for bingo_board in bingo_boards:
        print(bingo_board)

    print("last to win")
    print(winning_boards_details[-1])


def day4_b():
    pass


# day4_test_a()
# day4_a()
day4_test_b()
