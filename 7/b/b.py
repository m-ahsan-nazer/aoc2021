#!/usr/bin/python3.10
import unittest
from pprint import pprint
from typing import List, Dict, Tuple
import re
from math import sqrt, ceil, floor
import logging


def read_input_data(fname: str) -> Dict:
    """

    Returns
    -------
    input_data: Dict
    """
    input_data = dict()
    with open(fname, "r") as f:
        for line in f:
            line = f.readline().strip()
    return input_data


def perform_task(input_data: Dict):
    """
    Returns:
    --------
    num_pairs, int
    """
    task = ...
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

    @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input.txt")
        task = perform_task(input_data)


if __name__ == "__main__":
    unittest.main()
    # input_data = read_input_data("input.txt")
    # task = perform_task(input_data)
    # pprint(task)
