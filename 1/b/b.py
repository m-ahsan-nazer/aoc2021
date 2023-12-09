#!/usr/bin/python3.10
import unittest
from pprint import pprint
from typing import List
import re
import logging

DIGITS_DICT = dict(
    one="1",
    two="2",
    three="3",
    four="4",
    five="5",
    six="6",
    seven="7",
    eight="8",
    nine="9",
)


def find_replace_first_occurrence(s: str) -> str:
    replaced_number = ""
    replaced_number_index = len(s)
    for number in DIGITS_DICT:
        number_index = s.find(number)
        if number_index > -1:  # -1 is not found and false
            if number_index < replaced_number_index:
                replaced_number_index = number_index
                replaced_number = number
    s = s.replace(
        replaced_number, DIGITS_DICT.get(replaced_number, ""), 1
    )  # replace first occurrence only
    return s


def find_replace_last_occurrence(s: str) -> str:
    replaced_number = ""
    replaced_number_index = 0
    for number in DIGITS_DICT:
        number_index = s.rfind(number)
        if number_index > -1:  # -1 is not found and false
            if number_index > replaced_number_index:
                replaced_number_index = number_index
                replaced_number = number
    s = s[::-1].replace(replaced_number[::-1], DIGITS_DICT.get(replaced_number, ""), 1)
    return s[::-1]


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
            line = find_replace_first_occurrence(line)
            line = find_replace_last_occurrence(line)
            # Let ab be the two digit number
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
        self.assertListEqual(input_data, [29, 83, 13, 24, 42, 14, 76])

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 281)


if __name__ == "__main__":
    # unittest.main()
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
    # 53580 is too low
