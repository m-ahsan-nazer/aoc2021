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
            line = line.strip("\n")
            input_data.append([ch for ch in line])
    operations = input_data[-1]
    del input_data[-1]
    return (operations, input_data)


def solution(input_data: input_data_type):
    """
    What is the grand total found by adding together all of the answers to the individual problems?
    """
    operations, input_data = input_data
    operations = [s for s in operations if s != " "]
    transposed_input_data = list(zip(*input_data))
    transposed_input_data = ["".join(ch) for ch in transposed_input_data]
    transposed_input_data = [s.replace(" ", "") for s in transposed_input_data]
    logger.debug(f"data\n {transposed_input_data}")
    logger.debug(f"operations\n {operations}")
    problems = []
    solutions = []

    problem = []
    for i, ch in enumerate(transposed_input_data):
        if ch:
            problem.append(int(ch))
        else:
            problems.append(problem)
            problem = []

    problems.append(problem)
    logger.debug(f"problems: \n {problems}")
    for i, op in enumerate(operations):
        if op == "+":
            solutions.insert(i, 0)
        elif op == "*":
            solutions.insert(i, 1)
    for i, problem in enumerate(problems):
        op = operations[i]
        for j in problem:
            if op == "+":
                solutions[i] += int(j)
            elif op == "*":
                solutions[i] *= int(j)
    logger.debug(f"solutions: \n {solutions}")
    ans = sum(solutions)
    return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        return super().setUp()

    def test_read_input(self):
        input_file = "test_input.txt"
        operations, input_data = read_input(input_file)

        self.assertEqual(operations, [ch for ch in "*   +   *   +  "])
        self.assertEqual(
            input_data[0],
            ["1", "2", "3", " ", "3", "2", "8", " ", " ", "5", "1", " ", "6", "4", " "],
        )

    def test_solution(self):
        input_file = "test_input.txt"
        input_data = read_input(input_file)
        ans = solution(input_data)

        self.assertEqual(ans, 3263827)


if __name__ == "__main__":
    # unittest.main(verbosity=3, failfast=True)

    input_file = "input.txt"
    input_data = read_input(input_file)
    ans = solution(input_data)
    print(f"ans: {ans}")
