#!/usr/bin/python3.10
import unittest
from pprint import pprint
from typing import List
import logging

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

def extrapolate(l: List)->List:
    l_len_initial = len(l)
    l_diff = l.copy()
    l_diff.append(0)
    while True:
        l_diff = [l_diff[i+1]-l_diff[i] for i in range(len(l_diff)-1)]
        if l_diff[0:-1].count(0) == len(l_diff)-1: #all zeroes
            break
    return [*l,-l_diff[-1]]

def perform_task(input_data: List):
    """
    What is the sum of these extrapolated values?
    Returns:
    --------
    task, int
        Sum of these extrapolated values.
    """
    task = 0
    for l in input_data:
        task +=extrapolate(l)[-1]
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
        self.assertListEqual(
            input_data,
            [[0, 3, 6, 9, 12, 15], [1, 3, 6, 10, 15, 21], [10, 13, 16, 21, 30, 45]],
        )

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input.txt")
        task = perform_task(input_data)
        self.assertEqual(task,114)


if __name__ == "__main__":
    # unittest.main()
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
