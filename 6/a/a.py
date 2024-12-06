#!/usr/bin/python3.12
import logging
import re
import unittest
from itertools import pairwise
from pathlib import Path
import numpy as np
import pysnooper
from pprint import pprint
from typing import List, Tuple,Dict


input_data_type = Tuple[Dict,Tuple[int,int]]
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
OBSTRUCTION = "#"
EMPTY = "."

class Directions:
    UP = UP
    DOWN = DOWN
    LEFT = LEFT
    RIGHT = RIGHT

# @pysnooper.snoop()
def read_input_data_2(fname: str) -> input_data_type:
    """
    Returns
    -------
    input_data:
    """
    puzzle_map = dict()
    with open(Path(__file__).parent / fname, "r", encoding="utf-8") as f:
        row =0
        for line in f:
            line = line.strip()
            for col in range(len(line)):
                ch = line[col]
                puzzle_map[(row,col)] = ch
                if ch == "^":
                    origin = (row,col)
                

    return (puzzle_map, origin) 


def read_input_data(fname: str) -> np.ndarray:
    """
    Returns
    -------
    input_data:
    """
    puzzle_map = [] 
    with open(Path(__file__).parent / fname, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            puzzle_map.append(list(line))    
    puzzle_map = np.array(puzzle_map)
    (x,y)= np.argwhere(puzzle_map == "^")
    origin = (x[0], y[0])
    return (puzzle_map, origin)

def rotate_right(direction: Tuple[int,int])->Tuple[int,int]:
    match direction:
        case Directions.LEFT:
            return UP
        case Directions.RIGHT:
            return DOWN
        case Directions.UP:
            return RIGHT
        case Directions.DOWN:
            return LEFT
        case _:
            raise ValueError("Homie messed up")

def get_new_coords_from_direction(loc: Tuple[int,int], direction: Tuple[int,int], bounds: Tuple[int,int]) -> Tuple[int,int]:
    (num_rows, num_cols) = bounds
    (x, y) = (loc[0] +  direction[0], loc[1] +  direction[1])
    if x < 0 or x >= num_rows:
        return (np.inf, np.inf)
    
    if y < 0 or y >= num_cols:
        return (np.inf, np.inf)
    return (x, y)

def move(puzzle_map: np.ndarray, loc: Tuple[int,int], direction: Tuple[int,int]) -> Tuple[int,int]:
    """
    Returns
    -------
    coordinates of next step
    """
    (num_rows, num_cols) = puzzle_map.shape
    (x, y) = get_new_coords_from_direction(loc=loc,direction=direction,bounds=puzzle_map.shape)
    if x is np.inf:
        return (x,y)
    
    if puzzle_map[x,y] == OBSTRUCTION:
        new_direction = rotate_right(direction)

# @pysnooper.snoop()
def is_page_ordering_correct(rules: dict, page_ordering: list) -> bool:
    for p1 in rules:
        if p1 in page_ordering:
            for p2 in rules[p1]:
                if p2 in page_ordering and page_ordering.index(
                    p1
                ) > page_ordering.index(p2):
                    return False
    return True


def perform_task(input_data: input_data_type):
    """
    Returns:
    --------
    task, int
        What do you get if you add up the middle page number from those correctly-ordered updates?
    """
    rules, page_ordering = input_data
    correctly_ordered_updates = []
    for po in page_ordering:
        if is_page_ordering_correct(rules, po):
            correctly_ordered_updates.append(po)
    task = 0
    for po in correctly_ordered_updates:
        middle_ind = len(po) // 2
        task += po[middle_ind]

    return task


class TestTask(unittest.TestCase):
    def setUp(self) -> None:
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        return super().setUp()

    def test_sample_input(self):
        """
                Testing the input file.
        47|53
        97|13
        97|61
        97|47
        75|29
        61|13
        75|53
        29|13
        97|29
        53|29
        61|53
        97|53
        61|29
        47|13
        75|47
        97|75
        47|61
        75|61
        47|29
        75|13
        53|13
        """
        input_data = read_input_data("test_input_1.txt")

        rules, page_ordering = input_data
        self.assertSetEqual(set(rules[97]), set([13, 61, 47, 29, 53, 75]))
        self.assertSetEqual(set(rules[47]), set([53, 13, 61, 29]))

        self.assertListEqual(page_ordering[0], [75, 47, 61, 53, 29])
        self.assertListEqual(page_ordering[-1], [97, 13, 75, 29, 47])
        self.assertEqual(len(page_ordering), 6)

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input_1.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 143)


if __name__ == "__main__":
    # unittest.main(failfast=True)
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
