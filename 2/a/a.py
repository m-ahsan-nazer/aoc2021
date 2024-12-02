#!/usr/bin/python3.10
import logging
import re
import unittest
from itertools import pairwise
from pathlib import Path
from pprint import pprint
from typing import List, Tuple

input_data_type = List[List[int]]


def read_input_data(fname: str) -> input_data_type:
    """
    Returns
    -------
    input_data:
    """
    pattern = re.compile(r"\d+")
    input_data = []
    with open(Path(__file__).parent / fname, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            report = pattern.findall(line)
            report = [int(i) for i in report]
            input_data.append(report)

    return input_data


def perform_task(input_data: input_data_type):
    """
    Returns:
    --------
    task, int
        How many reports are safe?
    """
    task = 0
    safe_reports = []
    for report in input_data:
        (a, b) = (report[0], report[1])
        if a == b:
            diff_sign = 1
        else:
            diff_sign = (b - a) / abs(b - a)

        within_bound = False
        is_monotone = False
        for a, b in pairwise(report):
            within_bound = 1 <= abs(b - a) <= 3
            if not within_bound:
                break
            is_monotone = (b - a) / abs(b - a) == diff_sign
            if not is_monotone:
                break
        if is_monotone and within_bound:
            safe_reports.append(report)
    task = len(safe_reports)
    return task, safe_reports


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
        first_report = input_data[0]
        last_report = input_data[-1]
        self.assertListEqual(first_report, [7, 6, 4, 2, 1])
        self.assertListEqual(last_report, [1, 3, 6, 7, 9])

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input_1.txt")
        task, safe_reports = perform_task(input_data)
        self.assertEqual(task, 2)


if __name__ == "__main__":
    # unittest.main(failfast=True)
    input_data = read_input_data("input.txt")
    task, _ = perform_task(input_data)
    pprint(task)
