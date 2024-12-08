#!/usr/bin/python3.12
import logging
import re
import unittest
from itertools import pairwise, combinations
from pathlib import Path
import numpy as np
import pysnooper
from pprint import pprint
from typing import List, Tuple, Dict, Set, NewType
import dataclasses


input_data_type = Tuple[Dict[Tuple[int, int], str], Tuple[int, int]]

PointType = NewType(name="PointType", tp=Tuple[int, int])
# @pysnooper.snoop()


class Point:
    def __init__(self, coords: PointType):
        self.coords = coords

    def __sub__(self, p2: "Point") -> "Point":
        (x1, y1) = self.coords
        p3 = -p2
        return self.__add__(p3)

    def __add__(self, p2: "Point") -> "Point":
        (x1, y1) = self.coords
        (x2, y2) = p2.coords
        return Point((x2 + x1, y2 + y1))

    def __eq__(self, p2: "Point") -> bool:
        (x1, y1) = self.coords
        (x2, y2) = p2.coords
        return x1 == x2 and y1 == y2

    def __repr__(self):
        return str(self.coords)

    def __neg__(self) -> "Point":
        (x1, y1) = self.coords
        return Point((-x1, -y1))

    def __pos__(self) -> "Point":
        return self

    def __mul__(self, i: int) -> "Point":
        """
        Scalar mutiplication
        """
        (x1, y1) = self.coords
        p2 = Point((x1 * i, y1 * i))
        return p2

    def __rmul__(self, i: int) -> "Point":
        return self.__mul__(i)


def read_input_data(fname: str) -> input_data_type:
    """
    Returns
    -------
    input_data:
    """
    input_data = dict()
    with open(Path(__file__).parent / fname, "r", encoding="utf-8") as f:
        row = 0
        for line in f:
            line = line.strip()
            for col in range(len(line)):
                ch = line[col]
                input_data[(row, col)] = ch
            row += 1

    shape = (row, len(line))  # numpy notation (num_row, num_col)
    return (input_data, shape)


def get_distance_squared_between_points(p1: PointType, p2: PointType) -> int:
    (x1, y1) = p1
    (x2, y2) = p2
    return (y2 - y1) ** 2 + (x2 - x1) ** 2


def get_distinct_antenna_frequencies(input_data_: input_data_type) -> Set[str]:
    input_data, shape = input_data_
    distinct_antenna_frequencies = set(input_data.values())
    distinct_antenna_frequencies.remove(".")
    return distinct_antenna_frequencies


def get_coords_from_frequency(
    input_data_: input_data_type, freq: str
) -> List[Tuple[int, int]]:
    """
    Find all coords for a given frequency in the map
    """
    input_data, shape = input_data_
    coords = []
    for coord in input_data:
        if input_data[coord] == freq:
            coords.append(coord)
    return coords


def get_coords_pairs_for_frequency(
    coords: List[PointType],
) -> List[Tuple[PointType, PointType]]:
    """
    Assume coords has been filtered on freq
    """
    coords_pairs = list(combinations(coords, 2))
    return coords_pairs


def get_antinodes_for_coords_pairs(
    coords_pairs: Tuple[PointType, PointType], input_data_: input_data_type
) -> List[PointType]:
    """
    After updating your model, it turns out that an antinode occurs at any grid
    position exactly in line with at least two antennas of the same frequency,
    regardless of distance. This means that some of the new antinodes will occur
    at the position of each antenna (unless that antenna is the only one of its frequency).
    """
    input_data, shape = input_data_
    p1, p2 = coords_pairs
    p1 = Point(p1)
    p2 = Point(p2)
    antinodes = [p1.coords, p2.coords]
    i = 1
    while True:
        p3 = p2 + i * (p2 - p1)
        if p3.coords in input_data:
            antinodes.append(p3.coords)
        else:
            break
        i += 1
    j = 1
    while True:
        p4 = p1 - j * (p2 - p1)
        if p4.coords in input_data:
            antinodes.append(p4.coords)
        else:
            break
        j += 1
    return antinodes


# @pysnooper.snoop()
def perform_task(input_data: input_data_type):
    """
    Returns:
    --------
    task, int
        How many unique locations within the bounds of the map contain an antinode?
    """
    task = 0
    distinct_antenna_frequencies = get_distinct_antenna_frequencies(
        input_data_=input_data
    )
    all_anti_nodes = set()
    for freq in distinct_antenna_frequencies:
        all_coords = get_coords_from_frequency(input_data_=input_data, freq=freq)
        all_coords_pairs = get_coords_pairs_for_frequency(coords=all_coords)
        for coords_pairs in all_coords_pairs:
            anti_nodes = get_antinodes_for_coords_pairs(
                coords_pairs=coords_pairs, input_data_=input_data
            )
            all_anti_nodes.update(anti_nodes)
    task = len(all_anti_nodes)
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
        input_data_, shape = read_input_data("test_input_1.txt")
        self.assertTupleEqual(shape, (12, 12))
        self.assertEqual(input_data_[(5, 6)], "A")
        self.assertEqual(input_data_[(1, 8)], "0")
        self.assertEqual(input_data_[(11, 11)], ".")

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input_1.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 34)


if __name__ == "__main__":
    # unittest.main(failfast=True)
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
