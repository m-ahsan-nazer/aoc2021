import logging
import re
import unittest
from pathlib import Path
from typing import Dict, List, Tuple

base_dir = Path(__file__).parent
logger = logging.getLogger(__name__)
logging.basicConfig(filename=base_dir / "debug.log", level=logging.DEBUG, filemode="w")

input_data_type = Tuple[List, List]
pattern = re.compile(r"[\d]+")


def read_input(input_file: str) -> input_data_type:
    input_data = []
    with open(base_dir / input_file, "r") as f:
        for line in f:
            line = line.strip("\n").strip().strip("\n")
            input_data.append(line)
    operations = input_data[-1]
    operations = operations.replace(" ", "")
    operations = [char for char in operations]
    for i in range(len(input_data) - 1):
        line = pattern.findall(input_data[i])
        input_data[i] = [int(num) for num in line]
    del input_data[i + 1]
    return (operations, input_data)


def solution(input_data: input_data_type):
    """
    What is the grand total found by adding together all of the answers to the individual problems?
    """
    operations, input_data = input_data
    cols = input_data[0]
    for row in input_data[1:]:
        for op, i, j in zip(operations, row, range(len(operations))):
            if op == "+":
                cols[j] += i
            elif op == "*":
                cols[j] *= i

    logger.debug(f"cols: \n {cols}")
    ans = sum(cols)
    return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_read_input(self):
        input_file = "test_input.txt"
        operations, input_data = read_input(input_file)
        self.assertEqual(operations, ["*", "+", "*", "+"])
        self.assertEqual(
            input_data, [[123, 328, 51, 64], [45, 64, 387, 23], [6, 98, 215, 314]]
        )

    def test_solution(self):
        input_file = "test_input.txt"
        input_data = read_input(input_file)
        ans = solution(input_data)

        self.assertEqual(ans, 4277556)


if __name__ == "__main__":
    # unittest.main(verbosity=3, failfast=True)

    input_file = "input.txt"
    input_data = read_input(input_file)
    ans = solution(input_data)
    print(f"ans: {ans}")
