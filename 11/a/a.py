#!/usr/bin/python3.10
import unittest
from pprint import pprint
from typing import List
import logging
import re


def read_input_data(fname: str) -> List:
    """
    Returns
    -------
    input_data: List
    """
    input_data = list()
    with open(fname, "r") as f:
        for line in f:
            line = line.strip().split(" ")
            line = [int(_) for _ in line]
            input_data.append(line)
    return input_data


def perform_task(input_data: List):
    """
    Expand the universe, then find the length of the shortest path 
    between every pair of galaxies. What is the sum of these lengths?
    Returns:
    --------
    task, int
        Sum of shortest paths.
    """
    task = 0
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
