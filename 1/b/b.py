#!/usr/bin/python3.10
import logging
import re
import unittest
from pathlib import Path
from pprint import pprint
from typing import List, Tuple

input_data_type = Tuple[list, list]


def read_input_data(fname: str) -> input_data_type:
    """
    Returns
    -------
    input_data:
    """
    pattern = re.compile(r"\d+")
    group_1_ids = []
    group_2_ids = []
    with open(Path(__file__).parent / fname, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # Let a, b be the integer ids
            a, b = pattern.findall(line)
            group_1_ids.append(int(a))
            group_2_ids.append(int(b))

    return (group_1_ids, group_2_ids)


def perform_task(input_data: input_data_type):
    """
    Returns:
    --------
    task, int
        What is their similarity score?
    """
    group_1_ids, group_2_ids = input_data
    task = 0
    for a in group_1_ids:
        task += group_2_ids.count(a)*a
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
        group_1_ids, group_2_ids = input_data
        self.assertListEqual(group_1_ids, [3, 4, 2, 1, 3, 3])

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input_1.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 31)


if __name__ == "__main__":
    # unittest.main(failfast=True)
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
