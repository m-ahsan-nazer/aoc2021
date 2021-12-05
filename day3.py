from typing import List, NewType
import unittest


CountsType = NewType("CountsType", List[List[int]])


def counts_from_input_file(fname: str) -> CountsType:
    with open(fname, "r") as f:
        line = f.readline()
        line_width = len(line.strip().strip("\n"))
        counts = [[0, 0] for i in range(line_width)]
        f.seek(0)

        for line in f:
            line = line.strip()
            for i, c in enumerate(line):
                if int(c):
                    counts[i][1] += 1
                else:
                    counts[i][0] += 1
    return counts


def counts_from_input_list(data: List[str]) -> CountsType:
    line_width = len(data[0].strip("\n"))
    counts = [[0, 0] for i in range(line_width)]
    for line in data:
        line = line.strip("\n")
        for i, c in enumerate(line):
            if int(c):
                counts[i][1] += 1
            else:
                counts[i][0] += 1
    return counts


def gamma_rate_from_counts(counts: CountsType) -> str:
    gamma_rate: str = ""
    for count in counts:
        zero_count, one_count = count
        if zero_count >= one_count:
            gamma_rate += "0"
        else:
            gamma_rate += "1"
    return gamma_rate


def epsilon_rate_from_counts(counts: CountsType) -> str:
    epsilon_rate: str = ""
    for count in counts:
        zero_count, one_count = count
        if zero_count <= one_count:
            epsilon_rate += "0"
        else:
            epsilon_rate += "1"
    return epsilon_rate


def oxygen_generator_rating_from_counts(
    counts: CountsType, data: List[str], i: int
) -> str:
    """
    i: data index
    """
    oxygen_generator_rating: str = ""
    if len(data) == 1:
        oxygen_generator_rating = data[-1].strip("\n")
        return oxygen_generator_rating

    count = counts.pop(i)
    zero_count, one_count = count
    if zero_count > one_count:
        data = filter(lambda line: line[i] == "0", data)
    else:
        data = filter(lambda line: line[i] == "1", data)
    data = list(data)
    counts = counts_from_input_list(data)
    oxygen_generator_rating = oxygen_generator_rating_from_counts(counts, data, i + 1)
    return oxygen_generator_rating


def co2_scrubber_rating_from_counts(counts: CountsType, data: List[str], i: int) -> str:
    """
    i: data index
    """
    co2_scrubber_rating: str = ""
    if len(data) == 1:
        co2_scrubber_rating = data[-1].strip("\n")
        return co2_scrubber_rating

    count = counts.pop(i)
    zero_count, one_count = count
    if zero_count <= one_count:
        data = filter(lambda line: line[i] == "0", data)
    else:
        data = filter(lambda line: line[i] == "1", data)
    data = list(data)
    counts = counts_from_input_list(data)
    co2_scrubber_rating = co2_scrubber_rating_from_counts(counts, data, i + 1)
    return co2_scrubber_rating


def test_a():
    test_data_a = """
    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010
    """
    lines = test_data_a.strip().split("\n")
    line_width = len(lines[0].strip().strip("\n"))
    counts = [[0, 0] for i in range(line_width)]

    for line in lines:
        line = line.strip()
        for i, c in enumerate(line):
            if int(c):
                counts[i][1] += 1
            else:
                counts[i][0] += 1

    gamma_rate = gamma_rate_from_counts(counts)
    epsilon_rate = epsilon_rate_from_counts(counts)
    print(f"gamma_rate={gamma_rate}")
    print(f"epsilon_rate={epsilon_rate}")
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(f"power consumption: {power_consumption}, {bin(power_consumption)}")


def day3_a():
    fname = "days/3/input.txt"
    with open(fname, "r") as f:
        line = f.readline()
        line_width = len(line.strip().strip("\n"))
        counts = [[0, 0] for i in range(line_width)]
        f.seek(0)

        for line in f:
            line = line.strip()
            for i, c in enumerate(line):
                if int(c):
                    counts[i][1] += 1
                else:
                    counts[i][0] += 1

        gamma_rate = gamma_rate_from_counts(counts)
        epsilon_rate = epsilon_rate_from_counts(counts)
        print(f"gamma_rate={gamma_rate}")
        print(f"epsilon_rate={epsilon_rate}")
        power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
        print(f"power consumption: {power_consumption}, {bin(power_consumption)}")


def test_b():
    fname = "days/3/test_input.txt"
    counts = counts_from_input_file(fname)
    gamma_rate = gamma_rate_from_counts(counts)
    epsilon_rate = epsilon_rate_from_counts(counts)
    print(f"gamma_rate={gamma_rate}")
    print(f"epsilon_rate={epsilon_rate}")
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(f"power consumption: {power_consumption}, {bin(power_consumption)}")

    input_file = open(fname, "r")
    lines = input_file.readlines()
    input_file.close()

    counts_from_list = counts_from_input_list(lines)
    counts_tc = unittest.TestCase()
    counts_tc.assertEqual(counts, counts_from_list)

    initial_lines = lines.copy()
    oxygen_generator_rating = oxygen_generator_rating_from_counts(
        counts.copy(), lines, 0
    )
    counts_tc.assertEqual(counts, counts_from_list)
    assert initial_lines == lines
    co2_scrubber_rating = co2_scrubber_rating_from_counts(counts.copy(), lines, 0)
    assert initial_lines == lines

    print(f"oxygen_generator_rating={oxygen_generator_rating}")
    print(f"co2_scrubber_rating={co2_scrubber_rating}")
    life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
    print(f"life_support_rating: {life_support_rating}")


def day3_b():
    print("\n************day3_b************")
    fname = "days/3/input.txt"
    counts = counts_from_input_file(fname)
    gamma_rate = gamma_rate_from_counts(counts)
    epsilon_rate = epsilon_rate_from_counts(counts)
    print(f"gamma_rate={gamma_rate}")
    print(f"epsilon_rate={epsilon_rate}")
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(f"power consumption: {power_consumption}, {bin(power_consumption)}")

    input_file = open(fname, "r")
    lines = input_file.readlines()
    input_file.close()

    oxygen_generator_rating = oxygen_generator_rating_from_counts(
        counts.copy(), lines, 0
    )
    co2_scrubber_rating = co2_scrubber_rating_from_counts(counts.copy(), lines, 0)

    print(f"oxygen_generator_rating={oxygen_generator_rating}")
    print(f"co2_scrubber_rating={co2_scrubber_rating}")
    life_support_rating = int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2)
    print(f"life_support_rating: {life_support_rating}")


# test_a()
# day3_a()
test_b()
day3_b()
