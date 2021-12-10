from typing import List, Tuple, Dict, NewType
from itertools import product
from pprint import pprint


def read_input_data(fname: str) -> List[str]:
    input_data = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip().strip("\n")
            input_data.append(line)
    return input_data


def get_brackets():
    o_brackets = "[,{,(,<".split(",")
    c_brackets = "],},),>".split(",")
    return {"o": o_brackets, "c": c_brackets}


def get_mirror(c: str) -> str:
    brackets = get_brackets()
    o_brackets = brackets.get("o")
    c_brackets = brackets.get("c")
    if c in o_brackets:
        ic = o_brackets.index(c)
        c_mirror = c_brackets[ic]
    elif c in c_brackets:
        ic = c_brackets.index(c)
        c_mirror = o_brackets[ic]
    else:
        raise Exception(f"{c} is not an opening or closing bracket")
    return c_mirror


def get_first_c_bracket(s: str) -> Tuple[str, int]:
    assert s != ""

    brackets = get_brackets()
    c_brackets = brackets.get("c")
    ics = []
    for c in c_brackets:
        if c in s:
            ic = s.index(c)
            ics.append(ic)
    if len(ics) >= 1:
        min_ic = min(ics)
        c = s[min_ic]
        return (c, min_ic)
    return (None, None)


def pop_oc_brackets_from_str(s: str, c: str, ic: int) -> str:
    ss = s[: ic - 1] + s[ic + 1 :]
    return ss


def get_missing_bracket(s: str) -> str:
    while len(s) >= 1:
        c, ic = get_first_c_bracket(s)
        if c is None:
            break
        has_matching_bracket = check_has_matching_bracket(s, c, ic)
        if has_matching_bracket:
            s = pop_oc_brackets_from_str(s, c, ic)
        else:
            break
    # if c is None:
    # return get_mirror(s[-1])
    return c


def get_incomplete_line(s: str) -> str:
    while len(s) >= 1:
        c, ic = get_first_c_bracket(s)
        if c is None:
            break
        has_matching_bracket = check_has_matching_bracket(s, c, ic)
        if has_matching_bracket:
            s = pop_oc_brackets_from_str(s, c, ic)
        else:
            break

    return s


def get_line_completing_brackets(s: str) -> str:
    line_completing_brackets = ""
    for o in s[::-1]:
        c = get_mirror(o)
        line_completing_brackets += c
    return line_completing_brackets


def get_completion_score(s: str) -> int:
    score = 0
    for c in s:
        if c == ")":
            score = score * 5 + 1
        elif c == "]":
            score = score * 5 + 2
        elif c == "}":
            score = score * 5 + 3
        elif c == ">":
            score = score * 5 + 4
    return score


def get_bracket_score(c: str) -> int:
    brackets = get_brackets()
    assert c in brackets["c"]

    if c == ")":
        return 3
    elif c == "]":
        return 57
    elif c == "}":
        return 1197
    elif c == ">":
        return 25137


def check_has_matching_bracket(s: str, c: str, ic: int) -> bool:
    assert s[ic] == c

    c_mirror = get_mirror(c)
    return s[ic - 1] == c_mirror


def day10_test_a():
    fname = "days/10/test_input.txt"
    input_data = read_input_data(fname)
    # line = input_data[0]
    line0 = "(]"
    line1 = "{()()()>"
    line2 = "(((()))}"
    line3 = "<([]){()}[{}])"
    # line = line3
    # print("line: ", line)
    # c, ic = get_first_c_bracket(line)
    # print(c, ic)
    # has_matching_bracket = check_has_matching_bracket(line, c, ic)
    # print(f"has_matching_bracket: {has_matching_bracket}")
    total_score = 0
    for line in input_data:
        c = get_missing_bracket(line)
        if c is None:
            continue
        score = get_bracket_score(c)
        print(f"score {c}: ", score)
        total_score += score

    print(f"total score: {total_score}")


def day10_a():
    fname = "days/10/input.txt"
    input_data = read_input_data(fname)
    # line = input_data[0]
    line0 = "(]"
    line1 = "{()()()>"
    line2 = "(((()))}"
    line3 = "<([]){()}[{}])"
    # line = line3
    # print("line: ", line)
    # c, ic = get_first_c_bracket(line)
    # print(c, ic)
    # has_matching_bracket = check_has_matching_bracket(line, c, ic)
    # print(f"has_matching_bracket: {has_matching_bracket}")
    total_score = 0
    for line in input_data:
        c = get_missing_bracket(line)
        if c is None:
            continue
        score = get_bracket_score(c)
        print(f"score {c}: ", score)
        total_score += score

    print(f"total score: {total_score}")


def day10_test_b():
    fname = "days/10/test_input.txt"
    input_data = read_input_data(fname)
    # line = input_data[0]
    line0 = "(]"
    line1 = "{()()()>"
    line2 = "(((()))}"
    line3 = "<([]){()}[{}])"
    total_score = 0
    for line in input_data:
        c = get_missing_bracket(line[0:])
        if c is not None:
            continue
        incomplete_line = get_incomplete_line(line)
        score = get_bracket_score(c)
        print(f"score {c}: ", score)
        total_score += score

    print(f"total score: {total_score}")


def day10_b():
    # fname = "days/10/input.txt"
    pass


# day10_test_a()
# day10_a()
day10_test_b()
# day10_b()
