from typing import Dict, List, Tuple, Set


def read_input_data(fname: str) -> List[str]:
    input_data = []
    with open(fname, "r") as f:
        for line in f:
            _, line = line.strip().strip("\n").split("|")
            line = line.split()
            input_data.append(line)
    return input_data


def read_input_data_b(fname: str) -> Tuple[List[str], List[str]]:
    signal_patterns_data = []
    four_digit_output_data = []
    with open(fname, "r") as f:
        for line in f:
            signal_patterns, four_digit_output = line.strip().strip("\n").split("|")
            signal_patterns = signal_patterns.strip().split()
            signal_patterns_data.append(signal_patterns)
            four_digit_output = four_digit_output.strip().split()
            four_digit_output_data.append(four_digit_output)

    return (signal_patterns_data, four_digit_output_data)


def day8_test_a():
    fname = "input.txt"
    input_data = read_input_data(fname)
    counts = 0
    for i, digits in enumerate(input_data):
        for digit in digits:
            if len(digit) in [2, 4, 3, 7]:
                counts += 1
    print(f"all counts: {counts}")


def a_contains_b(a: str, b: str) -> bool:
    for c in b:
        if c not in a:
            return False
    return True


def get_in_a_not_b(a: str, b: str) -> str:
    """
    a-b != b-a
    """
    in_a_not_b = ""
    for c in a:
        if c not in b:
            in_a_not_b += c
    return in_a_not_b


def get_seven_segment_from_pattern(pattern: str) -> str:
    seven_segments = ""
    return seven_segments


def get_patterns_with_len(line_pattern: List[str], num: int) -> Set:
    patterns_with_len = set()
    for p in line_pattern:
        if len(p) == num:
            patterns_with_len.add(p)
    return patterns_with_len


def get_decoded_patterns(line_pattern: List[str]) -> Dict:
    decoded_patterns = dict.fromkeys(line_pattern)

    one = get_patterns_with_len(decoded_patterns.keys(), 2)
    assert len(one) == 1
    one = one.pop()
    seven = get_patterns_with_len(decoded_patterns.keys(), 3)
    assert len(seven) == 1
    seven = seven.pop()
    four = get_patterns_with_len(decoded_patterns.keys(), 4)
    assert len(four) == 1
    four = four.pop()
    eight = get_patterns_with_len(decoded_patterns.keys(), 7)
    assert len(eight) == 1
    eight = eight.pop()

    two_three_five = get_patterns_with_len(decoded_patterns.keys(), 5)
    assert len(two_three_five) == 3

    zero_six_nine = get_patterns_with_len(decoded_patterns.keys(), 6)
    assert len(zero_six_nine) == 3

    # seven_minus_one = get_in_a_not_b(seven, one)
    four_minus_one = get_in_a_not_b(four, one)
    three = None
    five = None
    for p in two_three_five:
        if a_contains_b(p, one):
            three = p
        elif a_contains_b(p, four_minus_one):
            five = p
    assert three is not None
    assert five is not None
    two = two_three_five - set([three, five])
    assert len(two) == 1
    two = two.pop()

    six = None
    nine = None
    for p in zero_six_nine:
        if not a_contains_b(p, one):
            six = p
        elif a_contains_b(p, four):
            nine = p
    assert six is not None
    assert nine is not None
    zero = zero_six_nine - set([six, nine])
    assert len(zero) == 1
    zero = zero.pop()

    decoded_patterns[zero] = str(0)
    decoded_patterns[one] = str(1)
    decoded_patterns[two] = str(2)
    decoded_patterns[three] = str(3)
    decoded_patterns[four] = str(4)
    decoded_patterns[five] = str(5)
    decoded_patterns[six] = str(6)
    decoded_patterns[seven] = str(7)
    decoded_patterns[eight] = str(8)
    decoded_patterns[nine] = str(9)
    for value in decoded_patterns.values():
        assert value is not None
    return decoded_patterns


def day8_test_b():
    fname = "days/8/test_input.txt"
    input_data = read_input_data(fname)
    outputs = []
    for line in input_data:
        decoded_patterns = get_decoded_patterns(line)
        digits = ""
        for c in line:
            digits += decoded_patterns[c]
        outputs.append(digits)

    outputs = [int(c) for c in outputs]
    print(sum(outputs), outputs)


def get_digit_set_from_decoded_patterns(decoded_patterns: Dict) -> Dict:
    digit_set_from_decoded_patterns = {}
    for key, value in decoded_patterns.items():
        digit_set_from_decoded_patterns[value] = set(key)
    return digit_set_from_decoded_patterns


def day8_b():
    fname = "days/8/test_input.txt"
    signal_patterns_data, four_digit_output_data = read_input_data_b(fname)
    # input_data = [s + f for (s, f) in zip(signal_patterns_data, four_digit_output_data)]
    outputs = []
    for i, line_s in enumerate(signal_patterns_data):
        decoded_patterns = get_decoded_patterns(line_s)
        digit_set_from_decoded_patterns = get_digit_set_from_decoded_patterns(
            decoded_patterns
        )
        digits = ""
        for c in four_digit_output_data[i]:
            for key, value in digit_set_from_decoded_patterns.items():
                diff = value.difference(set(c))
                if len(diff) == 0:
                    print("diff: ", diff, len(diff))
                    digits += key
                    print("key: ", key)
        print("digig: ", digits)
        outputs.append(digits)

    outputs = [int(c) for c in outputs]
    print(sum(outputs), outputs)


if __name__ == "__main__":
    # day8_test_a()
    # day8_a()
    # day8_test_b()
    day8_b()
