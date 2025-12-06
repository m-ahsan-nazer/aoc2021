import logging
import unittest
from pathlib import Path
from typing import List
from itertools import cycle

base_dir = Path(__file__).parent
logger = logging.getLogger(__name__)
logging.basicConfig(filename=base_dir / "debug.log", level=logging.DEBUG)

input_data_type = List[int]


def read_input(input_file: str) -> input_data_type:
    input_data = []
    with open(base_dir / input_file, "r") as f:
        for line in f:
            line = line.strip("\n").strip()
            line = line.replace("L", "-")
            line = line.replace("R", "+")
            input_data.append(int(line))
    return input_data


def solution(input_data: input_data_type):
    """
    The number of times the dial is pointing at 0.
    """
    positions = list(range(0,100,1))
    current_pos = 50
    zero_count = 0
    for i in input_data:
        increment = i // abs(i)
        j = 0
        while j != i:
            current_pos += increment
            current_pos = current_pos % 100
            num = positions[current_pos]
            if num == 0:
                zero_count +=1
            j += increment
            
            
    ans = zero_count
    return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_read_input(self):
        input_file = "test_input.txt"
        input_data = read_input(input_file)
        self.assertEqual(input_data, [-68, -30, 48, -5, 60, -55, -1, -99, 14, -82])

    def test_solution(self):
        input_file = "test_input.txt"
        input_data = read_input(input_file)
        ans = solution(input_data)

        self.assertEqual(ans, 6)


if __name__ == "__main__":
    # unittest.main(verbosity=3, failfast=True)

    input_file = "input.txt"
    input_data = read_input(input_file)
    ans = solution(input_data)
    print(f"ans: {ans}")
