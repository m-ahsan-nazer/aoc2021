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


def get_initial_boards(pos1: int, pos2: int) -> Dict:
    boards = dict.fromkeys(product(range(10), range(10), range(0, 21)), 0)
    boards[pos1, pos2, 0] = 1
    return boards


def get_dirac_dice_rolls() -> List[int]:
    dirac_dice_rolls = product([1, 2, 3], [1, 2, 3], [1, 2, 3])
    dirac_dice_rolls = [sum(throw) for throw in dirac_dice_rolls]
    return dirac_dice_rolls


def get_steps() -> Dict:
    dice_rolls = get_dirac_dice_rolls()
    steps = {}
    for roll in dice_rolls:
        if steps.get(roll) is None:
            steps[roll] = 1
        else:
            steps[roll] += 1
    return steps


def perform_player_turn_v2(
    boards: Dict, player: int, wins: Dict = {1: 0, 2: 0}, winning_score=21
) -> Dict:
    steps = get_steps()
    new_boards = {}
    if player == 1:
        for board_id in boards:
            if boards.get(board_id):
                for step in steps:
                    pos1, pos2, score = board_id
                    new_pos = pos1 + step
                    new_score = score + (new_pos % 10) + 1
                    new_board_id = (new_pos, pos2, new_score)
                    num = new_boards.get(new_board_id, 0)
                    if new_score >= winning_score:
                        wins[1] += (num + boards.get(board_id)) * steps.get(step)
                        continue
                    new_boards[new_board_id] = (num + boards.get(board_id)) * steps.get(
                        step
                    )
    if player == 2:
        for board_id in boards:
            if boards.get(board_id):
                for step in steps:
                    pos1, pos2, score = board_id
                    new_pos = pos2 + step
                    new_score = score + (new_pos % 10) + 1
                    new_board_id = (pos1, new_pos, new_score)
                    num = new_boards.get(new_board_id, 0)
                    if new_score >= winning_score:
                        wins[2] += (num + boards.get(board_id)) * steps.get(step)
                        continue
                    new_boards[new_board_id] = (num + boards.get(board_id)) * steps.get(
                        step
                    )
    return new_boards


def print_boards(boards: Dict):
    print("#######################")
    for board in boards:
        if boards.get(board):
            pprint([board, boards[board]])


def day21_test_b():
    """
    board = [pos1, score1, pos2, score2]
    0<=pos<=9
    """
    fname = "days/21/test_input.txt"
    pprint(sum(get_steps().values()))
    boards = get_initial_boards(4 - 1, 8 - 1)
    print_boards(boards)
    wins = {1: 0, 2: 0}
    for i in range(7):
        boards = perform_player_turn_v2(boards, 1, wins=wins)
        pprint((wins, len(boards)))
        boards = perform_player_turn_v2(boards, 2, wins=wins)
        pprint((wins, len(boards)))
    # pprint(boards)


def day21_b():
    fname = "days/21/input.txt"


if __name__ == "__main__":
    # day21_test_a()
    # day21_a()
    day21_test_b()
    # day21_b()
