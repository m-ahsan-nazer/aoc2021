#!/usr/bin/python3.10
import unittest
from pprint import pprint
from typing import List
import logging
import re


def read_input_data(fname: str) -> List:
    """
    ???.### 1,1,3
    Returns
    -------
    input_data: List
    """
    input_data = list()
    with open(fname, "r") as f:
        for line in f:
            springs, sizes = line.strip().split(" ")
            sizes = sizes.split(",")
            sizes = [int(i) for i in sizes]
            input_data.append([springs, sizes])
    return input_data


def perform_task(input_data: List):
    """
    For each row, count all of the different arrangements of operational 
    and broken springs that meet the given criteria. What is the sum of those counts?
    Returns:
    --------
    task, int
        Sum of counts of arrangements
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
    # unittest.main()
    input_data = read_input_data("input.txt")
    unknowns = 0
    damaged_sizes=None
    puzzle = ""
    for springs, sizes in input_data:
        if springs.count('?') > unknowns:
            unknowns = springs.count('?')
            damaged_sizes = sizes
            puzzle = springs
    print(unknowns, 2**unknowns, damaged_sizes, puzzle)
    # task = perform_task(input_data)
    # pprint(task)
