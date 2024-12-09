#!/usr/bin/python3.12
import dataclasses
import logging
import re
import unittest
from itertools import combinations, pairwise
from pathlib import Path
from pprint import pprint
from typing import Dict, List, NewType, Set, Tuple

import numpy as np
import pysnooper

input_data_type = Tuple[str, List[int]]


def read_input_data(fname: str) -> input_data_type:
    """
    Returns
    -------
    input_data:
    """
    with open(Path(__file__).parent / fname, "r", encoding="utf-8") as f:
        row = 0
        for line in f:
            line = line.strip()
    return (line, [int(i) for i in line])


# @pysnooper.snoop()
def get_full_disk_map(input_data: input_data_type) -> List:
    """
    Full disk map.
    """
    full_disk_map = []
    input_data_str, input_data_list = input_data

    i = 0
    j = 0  # to count file group position
    while i < len(input_data_list):
        space_or_file_size = input_data_list[i]
        for k in range(space_or_file_size):
            if i % 2 == 0:
                full_disk_map.append(j)
            else:
                full_disk_map.append(None)
        if k == space_or_file_size - 1 and i % 2 == 0:
            j += 1
        i += 1
    return full_disk_map


def get_last_index_of_num(full_disk_map: List[int | None], skip: int) -> int:
    """
    Returns
    -------
    None or int
    """
    i = len(full_disk_map) - 1 - skip
    while i >= 0:
        if full_disk_map[i]:
            return i
        i -= 1
    return None


def get_disk_map_sizes(input_data: input_data_type) -> Tuple[int, int, int]:
    """
    Returns
    -------
    (used_space, free_space, disk_space)
    """
    _, data = input_data
    disk_space = sum(data)
    used_space = sum(data[0:None:2])
    free_space = sum(data[1:None:2])
    assert disk_space == used_space + free_space
    return (used_space, free_space, disk_space)


def get_check_sum(full_disk_map: List[int | None]) -> int:
    """
    To calculate the checksum, add up the result of multiplying each of
    these blocks' position with the file ID number it contains. The leftmost
    block is in position 0. If a block contains free space, skip it instead.
    """
    sum = 0
    for i in range(len(full_disk_map)):
        id = full_disk_map[i]
        if id:
            sum += i * id
    return sum


# @pysnooper.snoop(watch=('full_disk_map','disk_space', 'idx'))
def perform_task(input_data: input_data_type):
    """
    Returns:
    --------
    task, int
        What is the resulting filesystem checksum?
    """
    input_data_str, input_data_list = input_data
    task = 0
    full_disk_map = get_full_disk_map(input_data=input_data)
    (used_space, free_space, disk_space) = get_disk_map_sizes(input_data=input_data)

    skip = 0
    for i in range(disk_space):
        if full_disk_map[i] is None:
            idx = get_last_index_of_num(full_disk_map=full_disk_map, skip=skip)
            if idx < i:
                break
            num = full_disk_map[idx]
            full_disk_map[idx] = None
            full_disk_map[i] = num
            skip += 1
    task = get_check_sum(full_disk_map)
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
        s, l = input_data
        self.assertEqual(s, "2333133121414131402")

    # @pysnooper.snoop()
    def test_full_disk_map(self):

        input_data = read_input_data("test_input_1.txt")
        full_disk_map = get_full_disk_map(input_data=input_data)

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input_1.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 1928)


if __name__ == "__main__":
    # unittest.main(failfast=True)
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
