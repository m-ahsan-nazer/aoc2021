from typing import List, Dict, Tuple, NewType
from pprint import pprint
import copy
from itertools import cycle, product


def read_data_input(fname: str):
    funcs = []
    with open(fname, "r") as f:
        func = []
        f.readline()
        for line in f:
            line = line.strip().strip("\n")
            if "inp" in line:
                funcs.append(func)
                func = []
                continue
            func.append(line)
        funcs.append(func)

    return funcs


def add(a, b) -> int:
    a = a + b
    return a


def mul(a, b) -> int:
    a = a * b
    return a


def div(a, b) -> int:
    assert b != 0
    a = a // b
    return a


def mod(a, b) -> int:
    assert b != 0

    return a - div(a, b) * b


def eql(a, b) -> int:
    if a == b:
        return 1
    return 0


def perform_operation(s: str) -> int:
    operation, a, b = s.strip("").strip("\n").split(" ")
    a = int(a)
    b = int(b)

    if operation == "add":
        return add(a, b)
    if operation == "mul":
        return mul(a, b)
    if operation == "div":
        if b == 0:
            return None
        return div(a, b)
    if operation == "mod":
        if a < 0 or b <= 0:
            return None
        return mod(a, b)
    if operation == "eql":
        return eql(a, b)

    return None


def call_func(func: List, w: int = 0, x=0, y=0, z=0) -> int:
    values = dict.fromkeys("x,y,z,w".split(","), 0)
    values["w"] = w
    values["x"] = x
    values["y"] = y
    values["z"] = z
    for step in func:
        _, a, b = step.split(" ")
        # pprint(step)
        s = f"{_} {values[a]} {values.get(b, b)}"
        ans = perform_operation(s)
        if ans is None:
            return None
        values[a] = ans
        # pprint(s)
        # pprint(ans)
    # return {a: values.get(a)}
    return values


def day24_test_a():
    fname = "days/24/test_input.txt"
    funcs = read_data_input(fname)
    # pprint(funcs)
    func = funcs[0]
    ans = call_func(func, w=9)
    pprint(ans)


def get_max_valid_inp(func: List):
    for w in range(9, 0, -1):
        ans = call_func(func, w=w)
        if ans:
            return ans
    return ""


def day24_a():
    fname = "days/24/input.txt"
    funcs = read_data_input(fname)
    model_num = ""
    # for func in funcs[-1:-2]:
    w = 0
    x = 0
    y = 0
    z = 0
    # for func in funcs[0:1]:
    for func in funcs:
        # print(func)
        max_valid_inp = call_func(func, w, x, y, z)
        w = max_valid_inp.get("w")
        x = max_valid_inp.get("x")
        y = max_valid_inp.get("y")
        z = max_valid_inp.get("z")
        model_num += str(w)
        pprint(max_valid_inp)

    print("model_num: ", model_num)


def day24_test_b():
    """ """
    fname = "days/24/test_input.txt"


def day24_b():
    fname = "days/24/input.txt"


if __name__ == "__main__":
    # day24_test_a()
    day24_a()
    # day24_test_b()
    # day24_b()
