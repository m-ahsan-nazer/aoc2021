#!/usr/bin/python3.10
import unittest
from pprint import pprint
from typing import List
import logging
import re


def read_input_data(fname: str) -> List:
    """
    row=97, col=102 for S in input.txt
    row=3, col=1 for test_input.txt
    Compass 
            N
        W       E
            S

    The pipes are arranged in a two-dimensional grid of tiles:

    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east. └
    J is a 90-degree bend connecting north and west.  ┘
    7 is a 90-degree bend connecting south and west. ┐
    F is a 90-degree bend connecting south and east. ┌
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, 
    but your sketch doesn't show what shape the pipe has.
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
    Find the single giant loop starting at S. 
    How many steps along the loop does it take to get 
    from the starting position to the point farthest from the starting position?
    Returns:
    --------
    task, int
        Num steps from S to farthest point.
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
