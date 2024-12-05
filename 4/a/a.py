#!/usr/bin/python3.12
import logging
import re
import unittest
from itertools import pairwise
from pathlib import Path
import numpy as np
from pprint import pprint
from typing import List, Tuple


input_data_type = List[List[str]]
origin_type = Tuple[int, int]


def read_input_data(fname: str) -> input_data_type:
    """
    Returns
    -------
    input_data:
    """
    input_data = []
    with open(Path(__file__).parent / fname, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            input_data.append(list(line))
    return input_data


def get_square_edges_diagonals_2(
    origin: origin_type, input_data_array: np.ndarray
) -> Tuple[np.ndarray]:
    """
    Assume origin=(a,b) is the top-left corner of the square.
    ---> +x
    |
    v +y
    """
    (a, b) = origin
    width = len("XMAS")
    top = input_data_array[a, b : b + width]
    bot = input_data_array[a + width - 1, b : b + width]
    left = input_data_array[a : a + width, b]
    right = input_data_array[a : a + width, b + width - 1]
    d1 = input_data_array.diagonal()
    d2 = np.flipud(input_data_array).diagonal()
    return (top, bot, left, right, d1, d2)


def get_xmas_square(origin: origin_type, input_data_array: np.ndarray) -> np.ndarray:
    (a, b) = origin
    width = len("XMAS")
    xmas_square = input_data_array[b : b + width, a : a + width]
    return xmas_square


def get_square_edges_diagonals(xmas_square: np.ndarray) -> Tuple[np.ndarray]:
    """
    Assume origin=(a,b) is the top-left corner of the square.
    ---> +x
    |
    v +y
    """
    (a, b) = (0, 0)
    width = len("XMAS")
    top = xmas_square[a, b : b + width]
    bot = xmas_square[a + width - 1, b : b + width]
    left = xmas_square[a : a + width, b]
    right = xmas_square[a : a + width, b + width - 1]
    d1 = xmas_square.diagonal()
    d2 = np.flipud(xmas_square).diagonal()
    return (top, bot, left, right, d1, d2)


def perform_task(input_data: input_data_type):
    """
    Returns:
    --------
    task, int
        How many times does XMAS appear?
    """
    input_data_array = np.array(input_data)
    XMAS = "XMAS"
    task = 0
    xmas_square = get_xmas_square(origin=(6, 3), input_data_array=input_data_array)
    (top, bot, left, right, d1, d2) = get_square_edges_diagonals(
        xmas_square=xmas_square
    )
    (num_row, num_col) = input_data_array.shape
    for x in range(num_col - len(XMAS)):
        for y in range(num_row - len(XMAS)):
            xmas_square = get_xmas_square(
                origin=(x, y), input_data_array=input_data_array
            )
            (top, bot, left, right, d1, d2) = get_square_edges_diagonals(
                xmas_square=xmas_square
            )
            for edge_or_diag in (top, bot, left, right, d1, d2):
                if "".join(top) in [XMAS, XMAS[::-1]]:
                    task += 1
    return task


class TestTask(unittest.TestCase):
    def setUp(self) -> None:
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        return super().setUp()

    def test_sample_input(self):
        """
        Testing the input file.
        """
        input_data = read_input_data("test_input_1.txt")
        self.assertListEqual(input_data[0], list("MMMSXXMASM"))

    def test_get_square_edges_diagonals(self):
        input_data = read_input_data("test_input_1.txt")
        input_data_array = np.array(input_data)
        """
        MMMS
        MSAM        
        AMXS
        MSAM
        """
        xmas_square = get_xmas_square(origin=(0, 0), input_data_array=input_data_array)
        (top, bot, left, right, d1, d2) = get_square_edges_diagonals(
            xmas_square=xmas_square
        )
        self.assertListEqual(top.tolist(), list("MMMS"))
        self.assertListEqual(bot.tolist(), list("MSAM"))
        self.assertListEqual(left.tolist(), list("MMAM"))
        self.assertListEqual(right.tolist(), list("SMSM"))
        self.assertListEqual(d1.tolist(), list("MSXM"))
        self.assertListEqual(d2.tolist(), list("MMAS"))
        """
        MSMX
        XAMM
        XAMA
        SXSS
        input_data_array[3:3+4,6:6+4]
        """
        xmas_square = get_xmas_square(origin=(6, 3), input_data_array=input_data_array)
        (top, bot, left, right, d1, d2) = get_square_edges_diagonals(
            xmas_square=xmas_square
        )
        self.assertListEqual(top.tolist(), list("MSMX"))
        self.assertListEqual(bot.tolist(), list("SXSS"))
        self.assertListEqual(left.tolist(), list("MXXS"))
        self.assertListEqual(right.tolist(), list("XMAS"))
        self.assertListEqual(d1.tolist(), list("MAMS"))
        self.assertListEqual(d2.tolist(), list("SAMX"))

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input_1.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 18)


if __name__ == "__main__":
    unittest.main(failfast=True)
    # input_data = read_input_data("input.txt")
    # task = perform_task(input_data)
    # pprint(task)
