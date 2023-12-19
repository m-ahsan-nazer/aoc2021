#!/usr/bin/python3.10
import unittest
from pprint import pprint
from typing import List, Dict
import logging
import re


def read_input_data(fname: str) -> Dict:
    """
    px{a<2006:qkq,m>2090:A,rfg}
    {x=787,m=2655,a=1222,s=2876}
    Returns
    -------
    input_data: Dict
    """
    input_data = dict()
    workflow_pattern = re.compile(r"(\w+)\{(.*?)\}")
    ratings_pattern = re.compile(
        r"\{(?:x=)(?P<x>\d+),(?:m=)(?P<m>\d+),(?:a=)(?P<a>\d+),(?:s=)(?P<s>\d+)\}"
    )
    ratings = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            if workflow_pattern.match(line):
                workflow_name, instructions = workflow_pattern.match(line).groups()
                instructions = instructions.split(",")
                # instructions = [[condition, name],...[name]]
                instructions = [tuple(_.split(":")) for _ in instructions[:-1]] + [
                    instructions[-1]
                ]
                input_data[workflow_name] = instructions
            elif line == "":
                continue
            else:
                line = line[1:-1]
                ratings.append(eval(f"dict({line})"))
    input_data["ratings"] = ratings
    return input_data


def perform_task(input_data: List):
    """
    what do you get if you add together all of the rating numbers for all of the parts that ultimately get accepted?
    Returns:
    --------
    task, int
        sum of accepted ratings
    """
    task = 0
    ratings = input_data["ratings"]
    for rating in ratings:
        for key in rating:
            exec(f"{key}={rating[key]}")

        name = "in"
        while True:
            workflow = input_data[name]
            for condition, to_name in workflow[:-1]:
                if eval(condition):
                    name = to_name
                    break
            if name != to_name:  # no conditions satisfied go to default
                name = workflow[-1]
            if name == "A":
                rating["A"] = True
                break
            if name == "R":
                rating["R"] = True
                break
        exec("del x, m, a, s")
    accepted_ratings_filter = filter(lambda d: d.get("A"), ratings)
    for dic in accepted_ratings_filter:
        task += dic["x"] + dic["m"] + dic["a"] + dic["s"]
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
        input_data = read_input_data("test_input.txt")
        ratings = input_data["ratings"]
        self.assertDictEqual(ratings[0], dict(x=787, m=2655, a=1222, s=2876))
        self.assertDictEqual(ratings[-1], dict(x=2127, m=1623, a=2188, s=1013))

        # px{a<2006:qkq,m>2090:A,rfg}
        self.assertListEqual(
            input_data["px"], [("a<2006", "qkq"), ("m>2090", "A"), "rfg"]
        )

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 19114)


if __name__ == "__main__":
    # unittest.main()
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
