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
def read_input_data(fname: str) -> input_data_type:
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
            row+=1
                

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


def move(puzzle_map: np.ndarray, loc: Tuple[int,int], direction: Tuple[int,int]) -> Tuple[Tuple[int,int], Tuple[int,int]] | None:
    """
    Returns
    -------
    coordinates of next step and the direction
    """
    new_coord =  (loc[0] +  direction[0], loc[1] +  direction[1])
    if new_coord not in puzzle_map:
        return None
    if puzzle_map[new_coord] == OBSTRUCTION:
        direction = rotate_right(direction)
        new_coord =  (loc[0] +  direction[0], loc[1] +  direction[1])
        if new_coord not in puzzle_map:
            return None
        return (new_coord, direction)
    elif puzzle_map[new_coord] in [EMPTY, "^"]:
        return new_coord, direction

# @pysnooper.snoop()
def perform_task(input_data: input_data_type):
    """
    Returns:
    --------
    task, int
        How many distinct positions will the guard visit before leaving the mapped area?
    """
    task = 0
    visited_positions = set()
    (puzzle_map, origin)  = input_data
    visited_positions.add(origin)
    loc = origin
    direction = UP
    while True:
        new_coord_and_direction = move(puzzle_map=puzzle_map, loc=loc, direction=direction)
        if not new_coord_and_direction:
            break
        (loc , direction) = new_coord_and_direction
        visited_positions.add(loc)
    task = len(visited_positions)
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
        (puzzle_map, origin)  = input_data
        self.assertTupleEqual(origin,(6,4))

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input_1.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 41)


if __name__ == "__main__":
    # unittest.main(failfast=True)
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
