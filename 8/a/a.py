#!/usr/bin/python3.10
import unittest
from pprint import pprint
from typing import List, Dict, Tuple
import re
from math import sqrt, ceil, floor
import logging
from itertools import cycle
from collections import OrderedDict


def read_input_data(fname: str) -> Dict:
    """

    Returns
    -------
    input_data: Dict
    """
    pattern = re.compile(r"(\w+) = \((\w+), (\w+)\)")  # .fullmatch(s).groups()
    input_data = OrderedDict()
    with open(fname, "r") as f:
        left_right = list(f.readline().strip().replace("L", "0").replace("R", "1"))
        left_right = [int(lr) for lr in left_right]
        input_data["lr"] = cycle(left_right)
        f.readline()
        for line in f:
            line = line.strip()
            key, l, r = pattern.fullmatch(line).groups()
            input_data[key] = (l, r)
    return input_data


def perform_task(input_data: OrderedDict):
    """
    How many steps are required to reach ZZZ?
    Returns:
    --------
    task, int
        num of steps to reach ZZZ
    """
    task = 0
    lr = input_data.pop("lr")
    task = 0
    # node = next(iter(input_data))
    node = "AAA"
    while True:
        node = input_data.get(node)[next(lr)]
        task += 1
        if node == "ZZZ":
            break
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
        lr = input_data.pop("lr")
        self.assertListEqual([next(lr), next(lr), next(lr), next(lr)], [0, 0, 1, 0])

        self.assertDictEqual(
            input_data,
            dict(AAA=("BBB", "BBB"), BBB=("AAA", "ZZZ"), ZZZ=("ZZZ", "ZZZ")),
        )

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 6)


if __name__ == "__main__":
    # unittest.main()
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
