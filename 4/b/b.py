#!/usr/bin/python3.12
import logging
import re
import unittest
from itertools import pairwise
from pathlib import Path
from pprint import pprint
from typing import List, Tuple

input_data_type = List[Tuple[int, int]]


def remove_ignored_mult(instructions: str) -> str:
    DONOT = "don't()"
    DO = "do()"
    l, sep, r = instructions.partition(DONOT)
    if sep == "":
        return l
    elif sep is DONOT:
        rl, sep, rr = r.partition(DO)
        if sep == "":
            return l
        elif sep == DO:
            return l + rr


def read_input_data(fname: str) -> input_data_type:
    """
    Returns
    -------
    input_data:
    """
    instructions = ""
    with open(Path(__file__).parent / fname, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            instructions += line

    while True:
        new_instructions = remove_ignored_mult(instructions)
        if new_instructions == instructions:
            break
        instructions = new_instructions

    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    input_data = pattern.findall(instructions)
    input_data = [eval(s[4:-1]) for s in input_data]
    return input_data


def perform_task(input_data: input_data_type):
    """
    Returns:
    --------
    task, int
        what do you get if you add up all of the results of just the enabled multiplications?
    """

    task = 0
    for a, b in input_data:
        task += a * b
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
        self.assertListEqual(input_data, [(2, 4), (8, 5)])

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input_1.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 48)


if __name__ == "__main__":
    # unittest.main(failfast=True)
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
