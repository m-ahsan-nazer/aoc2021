#!/usr/bin/python3.10
import unittest
from pprint import pprint
from typing import List, Dict, Tuple
import re
from math import sqrt, ceil, floor
import logging


def read_input_data(fname: str) -> Dict:
    """
    Time:      7  15   30
    Distance:  9  40  200

    Returns
    -------
    input_data: Dict
    """
    TIME_PATTERN = re.compile(r"[\d]+")
    DISTANCE_PATTERN = re.compile(r"[\d]+")
    input_data = dict()
    with open(fname, "r") as f:
        line = f.readline().strip()
        input_data["time"] = [int(_) for _ in TIME_PATTERN.findall(line)]
        line = f.readline().strip()
        input_data["distance"] = [int(_) for _ in DISTANCE_PATTERN.findall(line)]
    return input_data


def get_roots(t0: int, d_star: int) -> Tuple:
    sqrt_discriminant = sqrt(t0 * t0 - 4 * d_star)
    epsilon = 1e-3
    roots = (
        (t0 - sqrt_discriminant) / 2.0 + epsilon,
        (t0 + sqrt_discriminant) / 2.0 - epsilon,
    )
    return roots


def get_start_times_that_beat_record(roots: Tuple) -> List:
    return list(range(ceil(roots[0]), floor(roots[1]) + 1))


def perform_task(input_data: Dict):
    """
    Determine the number of ways you could beat the record in each race.
    What do you get if you multiply these numbers together?

    Let t0 be the time to finish the race.
    Let d_star be the distance to beat.
    speed=distance/time, distance=speed*time
    Let t be the elapsed time.
    d=t*(t0-t), dd_dt=t0-2t, For t0-2t=0, we have t=t0/2.
    d_max = t0/2*(t0-t0/2)=t0**2/4
    Solving d_star = t*(t0-t) this for t gives
    (1/2)*t0-(1/2)*sqrt(t0^2-4*d_star), (1/2)*t0+(1/2)*sqrt(t0^2-4*d_star)
    Solution:
    ---------
    Given that d=t*(t0-t) is an upside down parabola with its maximum at
    t=t0/2, the integer times between the two roots are the answer.
    Returns:
    --------
    num_pairs, int
    """
    results = dict()
    start_times = dict()
    task = 1
    for t0, d_star in zip(input_data["time"], input_data["distance"]):
        roots = get_roots(t0=t0, d_star=d_star)
        start_times[(t0, d_star)] = get_start_times_that_beat_record(roots=roots)
        results[(t0, d_star)] = len(start_times[(t0, d_star)])
        task *= results[(t0, d_star)]
    return task, results, start_times


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
        self.assertEqual(len(input_data), 2)
        self.assertDictEqual(input_data, dict(time=[7, 15, 30], distance=[9, 40, 200]))

    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input.txt")
        task, results, start_times = perform_task(input_data)
        self.assertEqual(task, 288)


if __name__ == "__main__":
    # unittest.main()
    input_data = read_input_data("input.txt")
    task, _, _ = perform_task(input_data)
    pprint(task)
