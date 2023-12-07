#!/usr/bin/python3.10
import unittest
from pprint import pprint
from typing import List, Dict, Tuple
import re
from math import sqrt, ceil, floor
import logging


CARDS = "A,K,Q,J,T,9,8,7,6,5,4,3,2".split(",")[::-1]
RANKS, _ = list(zip(*enumerate(CARDS)))
CARDS_DICT = dict(zip(CARDS, RANKS))


def read_input_data(fname: str) -> Dict:
    """

    Returns
    -------
    input_data: Dict
    """
    pattern = re.compile(r"([\w]{5}) ([\d]+)")
    input_data = dict()
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            hand, bid = pattern.fullmatch(line).groups()
            input_data[hand] = int(bid)
    return input_data


def get_hand_type(hand: str) -> int:
    """
    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456
    """
    char_set = set(hand)
    char_counts_dic = dict()
    for char in char_set:
        char_counts_dic[char] = hand.count(char)
    char_counts = list(char_counts_dic.values())
    five_in_counts = 5 in char_counts
    four_in_counts = 4 in char_counts
    three_in_counts = 3 in char_counts
    two_in_counts = 2 in char_counts
    if five_in_counts:  # Five of a kind
        return 7 
    elif four_in_counts:  # Four of a kind
        return 6
    elif three_in_counts and two_in_counts:  # Full house
        return 5
    elif three_in_counts and not two_in_counts:  # Three of a kind
        return 4
    elif two_in_counts and char_counts.count(2) == 2:  # Two pair
        return 3
    elif two_in_counts and char_counts.count(2) == 1:  # One pair
        return 2
    return 1


def get_ranked_hands(input_data: Dict) -> List:
    """
    Returns:
    --------
    ordered_hands: List
        [("32T3K", type, 1, 0, 8, 1, 10), ]
    """
    hands = []
    for hand in input_data:
        hand_type = get_hand_type(hand)
        hands.append(
            (
                hand,
                hand_type,
                CARDS_DICT.get(hand[0]),
                CARDS_DICT.get(hand[1]),
                CARDS_DICT.get(hand[2]),
                CARDS_DICT.get(hand[3]),
                CARDS_DICT.get(hand[4]),
            )
        )
    hands.sort(key=lambda x: x[1:])
    # hands.reverse()
    return hands


def perform_task(input_data: Dict):
    """
    Returns:
    --------
    task, int
        Total winnings = sum(rank*bid)
    """
    task = 0
    ranked_hands = get_ranked_hands(input_data)
    for rank, ranked_hand in enumerate(ranked_hands, start=1):
        hand = ranked_hand[0]
        task += rank * input_data[hand]
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
        self.assertDictEqual(
            input_data,
            {"32T3K": 765, "T55J5": 684, "KK677": 28, "KTJJT": 220, "QQQJA": 483},
        )
        self.assertEqual(len(input_data), 5)

    # @unittest.skip("Skip when testing read_input_data")
    def test_perform_task(self):
        """
        Testing the task algorithm.
        """
        input_data = read_input_data("test_input.txt")
        task = perform_task(input_data)
        self.assertEqual(task, 6440)


if __name__ == "__main__":
    # unittest.main()
    input_data = read_input_data("input.txt")
    task = perform_task(input_data)
    pprint(task)
    #too high 250948756
