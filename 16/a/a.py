#!/usr/bin/python3.10
import unittest
from pprint import pprint
from typing import Dict, List, Tuple
import logging
import re
import anytree


def read_input_data(fname: str) -> Dict:
    """
    Let o denote outer boundary of the layout
    Returns
    -------
    input_data: Dict
    """
    input_data = dict()
    with open(fname, "r") as f:
        row: int = 0
        for line in f:
            line = line.strip()
            for col, char in enumerate(line):
                input_data[(row, col)] = char
            row += 1
    input_data["dim"] = (row, col + 1)
    return input_data


def get_velocities(
    layout: Dict, cur_position: Tuple[int, int], prev_velocity: Tuple[int, int]
) -> List[Tuple[int, int]]:
    """
    operators [., |, -, /. \]
    """
    cur_operator = layout[cur_position]
    vel_x, vel_y = prev_velocity
    next_velocities = []
    match (vel_x, vel_y), cur_operator:
        case _, ".":
            next_velocities.append((vel_x, vel_y))
        case (0, 1), "|":
            next_velocities.append((0, 1))
        case (0, -1), "|":
            next_velocities.append((0, -1))
        case (1, 0), "|":
            next_velocities.extend([(0, 1), (0, -1)])
        case (-1, 0), "|":
            next_velocities.extend([(0, 1), (0, -1)])
        case (0, 1), "-":
            next_velocities.extend([(-1, 0), (1, 0)])
        case (0, -1), "-":
            next_velocities.extend([(-1, 0), (1, 0)])
        case (1, 0), "-":
            next_velocities.append((1, 0))
        case (-1, 0), "-":
            next_velocities.append((-1, 0))
        case _, "/":
            next_velocities.append((vel_y, vel_x))
        case _, "\\":
            next_velocities.append((-vel_y, -vel_x))
    return next_velocities


def validate_velocities(
    layout: Dict, cur_position: Tuple[int, int], velocities: List[Tuple[int, int]]
) -> List:
    """
    Removes velocities (in place) that lead out of the layout
    """
    for vel_x, vel_y in velocities.copy():
        pos_x = cur_position[0] + vel_x
        pos_y = cur_position[1] + vel_y
        if layout.get((pos_x, pos_y), None) is None:
            velocities.remove((vel_x, vel_y))


def perform_task(input_data: Dict):
    """
    how many tiles end up being energized?
    Returns:
    --------
    task, int
        Num of energized tiles
    """
    task = 0
    (num_rows, num_cols) = input_data.pop("dim")
    cur_position = (0, 0)
    prev_velocity = (1, 0)
    root = anytree.Node(name=cur_position, prev_velocity=prev_velocity, velocities=[])
    nodes = [root]
    for t in range(num_rows * num_cols*5):
        for node in nodes:
            velocities = get_velocities(
                layout=input_data,
                cur_position=node.name,
                prev_velocity=node.prev_velocity,
            )
            validate_velocities(
                layout=input_data, cur_position=cur_position, velocities=velocities
            )
            node.velocities = velocities
            children_nodes = []
            for prev_velocity in velocities:
                pos_x, pos_y = cur_position
                vel_x, vel_y = prev_velocity
                cur_position = (pos_x + vel_x, pos_y + vel_y)
                child_node = anytree.Node(
                    name=cur_position, prev_velocity=prev_velocity, parent=node
                )
                children_nodes.append(child_node)
        nodes = children_nodes
    breakpoint()
    return task


class TestTask(unittest.TestCase):
    def setUp(self) -> None:
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        self.input_data = read_input_data("test_input.txt")
        self.dim = self.input_data.pop("dim")
        return super().setUp()

    def test_sample_input(self):
        """
        Testing the input file.
        """
        input_data = self.input_data
        (row, col) = self.dim
        self.assertTupleEqual((row, col), (10, 10))
        self.assertEqual(input_data[(0, 0)], ".")
        self.assertEqual(input_data[(0, 1)], "|")
        self.assertEqual(input_data[(row - 1, col - 1)], ".")

    def test_get_velocities(self):
        input_data = self.input_data
        cur_position = (0, 0)
        prev_velocity = (1, 0)
        velocities = get_velocities(
            layout=input_data, cur_position=cur_position, prev_velocity=prev_velocity
        )
        self.assertListEqual(velocities, [prev_velocity])

        cur_position = (0, 1)
        prev_velocity = (1, 0)
        velocities = get_velocities(
            layout=input_data, cur_position=cur_position, prev_velocity=prev_velocity
        )
        self.assertIn((0, 1), velocities)
        self.assertIn((0, -1), velocities)

    # @unittest.skip("Skip when testing read_input_data")
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
