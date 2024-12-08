#!/usr/bin/python3.12
import logging
import re
import unittest
from itertools import pairwise
from pathlib import Path
import numpy as np
import pysnooper
from pprint import pprint
from typing import List, Tuple, Dict


input_data_type = Dict[int, List[int]]


# @pysnooper.snoop()
def read_input_data(fname: str) -> input_data_type:
    """
    Returns
    -------
    input_data:
    """
    input_data = dict()
    pattern = re.compile(r"\d+")
    with open(Path(__file__).parent / fname, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            # 190: 10 19
            line = pattern.findall(line)
            line = [int(i) for i in line]
            input_data[line[0]] = line[1:]

    return input_data


# @pysnooper.snoop()
def get_perfect_tree_leaf_nodes(eqn: List[int]) -> List[int]:
    root = eqn[0]
    nodes = [root]
    for i in eqn[1:]:
        new_nodes = []
        for node in nodes:
            new_nodes.extend([node * i, node + i, int(str(node) + str(i))])
        nodes = new_nodes
    return nodes


# @pysnooper.snoop()
def perform_task(input_data: input_data_type):
    """
    Returns:
    --------
    task, int
        What is their total calibration result?
    """
    task = 0
    valid_eqns = []
    for test_value in input_data:
        eqn = input_data[test_value]
        leaf_nodes = get_perfect_tree_leaf_nodes(eqn=eqn)
        if test_value in leaf_nodes:
            valid_eqns.append(test_value)
    task = sum(valid_eqns)
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
        self.assertListEqual(input_data[190], [10, 19])
        self.assertListEqual(input_data[161011], [16, 10, 13])
        self.assertListEqual(input_data[292], [11, 6, 16, 20])

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input_1.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 11387)


if __name__ == "__main__":
    # unittest.main(failfast=True)
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
