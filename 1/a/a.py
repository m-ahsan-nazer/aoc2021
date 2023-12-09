#!/usr/bin/python3.10
import unittest
from pprint import pprint
from typing import List
import re
import logging


def read_input_data(fname: str) -> List:
    """
    On each line, the calibration value can be found by combining the
    first digit and the last digit (in that order) to form a single two-digit number.
        Returns
        -------
        input_data: Dict
    """
    # pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")  # .fullmatch(s).groups()
    pattern_1 = re.compile(r"\d")
    pattern_2 = re.compile(r"[0-9]")
    input_data = []
    with open(fname, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Let ab be the digits
            digits = pattern_2.findall(line)
            a, b = (digits[0], digits[-1])
            input_data.append(int(a + b))
    return input_data


def perform_task(input_data: List):
    """
    Returns:
    --------
    task, int
        calibration i.e sum of input_data list
    """
    task = sum(input_data)
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
        input_data = read_input_data("test_input.txt")
        self.assertListEqual(input_data, [12, 38, 15, 77])

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 142)


if __name__ == "__main__":
    # unittest.main()
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
