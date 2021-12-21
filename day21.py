from typing import List, Dict, Tuple, NewType
from pprint import pprint
import copy
from itertools import cycle, product

Boards = NewType("Boards", List[List[int]])


def read_data_input(fname: str):
    """
    iea: image enhancement algorithm
    """
    pass


def day21_test_a():
    fname = "days/21/test_input.txt"
    p1_board = cycle(range(1, 11))
    p2_board = cycle(range(1, 11))
    dice_rolls = cycle(range(1, 101))
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
        dice_throw = next(dice_rolls)
        dice_throw += next(dice_rolls)
        dice_throw += next(dice_rolls)
        for i in range(dice_throw - 1):
            next(p1_board)
        p1_score += next(p1_board)
        num_dice_rolls += 3
        if p1_score >= 1000:
            winner = 1
            break
        # p2
        dice_throw = next(dice_rolls)
        dice_throw += next(dice_rolls)
        dice_throw += next(dice_rolls)
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
    dice_rolls = cycle(range(1, 101))
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
        dice_throw = next(dice_rolls)
        dice_throw += next(dice_rolls)
        dice_throw += next(dice_rolls)
        for i in range(dice_throw - 1):
            next(p1_board)
        p1_score += next(p1_board)
        num_dice_rolls += 3
        if p1_score >= 1000:
            winner = 1
            break
        # p2
        dice_throw = next(dice_rolls)
        dice_throw += next(dice_rolls)
        dice_throw += next(dice_rolls)
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


def get_dirac_dice_rolls() -> List[int]:
    dirac_dice_rolls = product([1, 2, 3], [1, 2, 3], [1, 2, 3])
    dirac_dice_rolls = [sum(throw) for throw in dirac_dice_rolls]
    return dirac_dice_rolls


def perform_player_turn(
    boards: Boards, player: int, wins: List[int]
) -> Tuple[Boards, List[int]]:
    """
    board = [pos1, score1, pos2, score2]
    0<=pos<=9
    wins = [num_wins_player1, num_wins_player2]
    """
    dirac_dice_rolls = get_dirac_dice_rolls()

    new_boards = []
    winning_score = 9
    # winning_score = 21
    for board in boards:
        for roll in dirac_dice_rolls:
            new_board = board.copy()
            if player == 1:
                new_board[0] = (new_board[0] + roll) % 10
                new_board[1] += new_board[0] + 1
            elif player == 2:
                new_board[2] = (new_board[2] + roll) % 10
                new_board[3] += new_board[2] + 1
            if new_board[1] >= winning_score:
                wins[0] += 1
                continue
            elif new_board[3] >= winning_score:
                wins[1] += 1
                continue
            new_boards.append(new_board)
    return (new_boards, wins)


def day21_test_b():
    """
    board = [pos1, score1, pos2, score2]
    0<=pos<=9
    """
    fname = "days/21/test_input.txt"
    wins = [0, 0]
    boards = [[4 - 1, 0, 8 - 1, 0]]
    pprint(boards)
    for i in range(5):
        boards, wins = perform_player_turn(boards, 1, wins)
        boards, wins = perform_player_turn(boards, 2, wins)
        pprint((wins, len(boards)))
    # pprint(boards)

    # pprint(boards[0:50])
    # pprint(boards[-50:])


def day21_b():
    fname = "days/21/input.txt"


if __name__ == "__main__":
    # day21_test_a()
    # day21_a()
    day21_test_b()
    # day21_b()
