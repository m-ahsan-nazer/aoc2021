from typing import List, Dict, Tuple, NewType
from pprint import pprint
import copy
from itertools import cycle


def read_data_input(fname: str):
    """
    iea: image enhancement algorithm
    """
    pass


def day21_test_a():
    fname = "days/21/test_input.txt"
    p1_board = cycle(range(1, 11))
    p2_board = cycle(range(1, 11))
    dice_throws = cycle(range(1, 101))
    num_dice_rolls = 0
    p1_score = 0
    p2_score = 0

    # set initial positions
    for i in range(4):
        next(p1_board)
    for i in range(8):
        next(p2_board)
    winner = 0
    while True:
        # p1
        dice_throw = next(dice_throws)
        dice_throw += next(dice_throws)
        dice_throw += next(dice_throws)
        for i in range(dice_throw - 1):
            next(p1_board)
        p1_score += next(p1_board)
        num_dice_rolls += 3
        if p1_score >= 1000:
            winner = 1
            break
        # p2
        dice_throw = next(dice_throws)
        dice_throw += next(dice_throws)
        dice_throw += next(dice_throws)
        for i in range(dice_throw - 1):
            next(p2_board)
        p2_score += next(p2_board)
        if p2_score >= 1000:
            winner = 2
            break
        num_dice_rolls += 3

    if winner == 1:
        print(p2_score * num_dice_rolls)
    elif winner == 2:
        print(p1_score * num_dice_rolls)


def day21_a():
    fname = "days/21/input.txt"
    p1_board = cycle(range(1, 11))
    p2_board = cycle(range(1, 11))
    dice_throws = cycle(range(1, 101))
    num_dice_rolls = 0
    p1_score = 0
    p2_score = 0

    # set initial positions
    for i in range(6):
        next(p1_board)
    for i in range(9):
        next(p2_board)
    winner = 0
    while True:
        # p1
        dice_throw = next(dice_throws)
        dice_throw += next(dice_throws)
        dice_throw += next(dice_throws)
        for i in range(dice_throw - 1):
            next(p1_board)
        p1_score += next(p1_board)
        num_dice_rolls += 3
        if p1_score >= 1000:
            winner = 1
            break
        # p2
        dice_throw = next(dice_throws)
        dice_throw += next(dice_throws)
        dice_throw += next(dice_throws)
        for i in range(dice_throw - 1):
            next(p2_board)
        p2_score += next(p2_board)
        if p2_score >= 1000:
            winner = 2
            break
        num_dice_rolls += 3

    if winner == 1:
        print(p2_score * num_dice_rolls)
    elif winner == 2:
        print(p1_score * num_dice_rolls)


def day21_test_b():
    fname = "days/21/test_input.txt"


def day21_b():
    fname = "days/21/input.txt"


if __name__ == "__main__":
    # day21_test_a()
    day21_a()
    # day21_test_b()
    # day21_b()
