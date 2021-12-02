from pprint import pprint


def readInput(fname):
    lines = []
    with open(fname, "r") as f:
        for line in f:
            lines.append(line)
    return lines


def diff(array):
    array_diff = []
    for i in range(1, len(array)):
        array_diff.append(array[i] - array[i - 1])
    return array_diff


def test():
    array = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    array_diff = diff(array)
    array_diff_text = []
    for x in array_diff:
        if x > 0:
            array_diff_text.append("increased")
        else:
            array_diff_text.append("decreased")

    num_increases = array_diff_text.count("increased")
    print(f"{num_increases}")
    # pprint(array_diff_text)
    for x in zip(array_diff, array[1:], array_diff_text):
        pprint(x)


def testTriplets():
    array = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    array_triplets = []
    for i in range(2, len(array)):
        triplet = (array[i - 2], array[i - 1], array[i])
        array_triplets.append(triplet)
    array_triplets_sum = [sum(triplet) for triplet in array_triplets]
    # pprint(("array_triplets_sum", array_triplets_sum))
    array_diff = diff(array_triplets_sum)
    array_diff_text = []
    for x in array_diff:
        if x > 0:
            array_diff_text.append("increased")
        elif x == 0:
            array_diff_text.append("no change")
        else:
            array_diff_text.append("decreased")

    num_increases = array_diff_text.count("increased")
    print(f"{num_increases}")
    for x in zip(array_triplets_sum[1:], array_diff_text):
        pprint(x)


def day1():
    day1_input = readInput("days/1/input.txt")
    array = [int(x.strip()) for x in day1_input]
    array_diff = diff(array)
    array_diff_text = []
    for x in array_diff:
        if x > 0:
            array_diff_text.append("increased")
        else:
            array_diff_text.append("decreased")

    num_increases = array_diff_text.count("increased")
    print(f"{num_increases}")
    # pprint(array_diff_text)


def day1Triplets():
    day1_input = readInput("days/1/input.txt")
    array = [int(x.strip()) for x in day1_input]
    array_triplets = []
    for i in range(2, len(array)):
        triplet = (array[i - 2], array[i - 1], array[i])
        array_triplets.append(triplet)
    array_triplets_sum = [sum(triplet) for triplet in array_triplets]
    array_diff = diff(array_triplets_sum)
    array_diff_text = []
    for x in array_diff:
        if x > 0:
            array_diff_text.append("increased")
        elif x == 0:
            array_diff_text.append("no change")
        else:
            array_diff_text.append("decreased")

    num_increases = array_diff_text.count("increased")
    print(f"{num_increases}")
    for x in zip(array_triplets_sum[1:], array_diff_text):
        pprint(x)


# testTriplets()
day1Triplets()
# test()
