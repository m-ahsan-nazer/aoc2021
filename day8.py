from typing import List
def read_input_data(fname: str) -> List[str]:
    input_data =[]
    with open(fname, 'r') as f:
        for line in f:
            _, line = line.strip().strip("\n").split("|")
            line = line.split()
            input_data.append(line)
    return input_data

def day8_test_a():
    fname = "input.txt"
    input_data = read_input_data(fname)
    counts = 0
    for i, digits in enumerate(input_data):
        for digit in digits:
            if len(digit) in [2, 4, 3, 7]:
                counts+=1
    print(f"all counts: {counts}")

def day8_a():
    return

day8_test_a()


