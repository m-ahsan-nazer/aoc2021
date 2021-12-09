from typing import List


def read_input_data(fname: str) -> List[int]:
    initial_state = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip("\n")
            line = line.split(",")
            for c in line:
                initial_state.append(int(c))
    return initial_state


def tick_fish_clock(first_gen: bool, fish: List[int]) -> List[int]:
    if first_gen:
        fish = [(i - 1) % 9 for i in fish]
    else:
        fish = [(i - 1) % 7 for i in fish]

    return fish


def spawn_new_baby_fish(first_gen: bool, num_baby_fish: int) -> List[int]:
    new_baby_fish = []
    for i in range(num_baby_fish):
        if first_gen:
            new_baby_fish.append(8)
        else:
            new_baby_fish.append(6)
    return new_baby_fish


def day6_test_a():
    fname = "days/6/test_input.txt"
    fish = read_input_data(fname)
    first_gen_fish = []
    print("Initial state: ", fish)
    # for i in range(80):
    for i in range(18):
        zeros_count_fish = fish.count(0)
        zeros_count_first_gen_fish = first_gen_fish.count(0)
        fish = tick_fish_clock(first_gen=False, fish=fish)
        fish += spawn_new_baby_fish(
            first_gen=False, num_baby_fish=zeros_count_first_gen_fish
        )
        first_gen_fish = tick_fish_clock(first_gen=True, fish=first_gen_fish)
        first_gen_fish += spawn_new_baby_fish(
            first_gen=True, num_baby_fish=zeros_count_fish
        )
        # print(f"After {i:3}  days:", fish + first_gen_fish)
    print(f"all fish after {i+1} days: ", len(fish) + len(first_gen_fish))


def day6_a():
    fname = "days/6/input.txt"
    fish = read_input_data(fname)
    first_gen_fish = []
    print("Initial state: ", fish)
    for i in range(80):
        zeros_count_fish = fish.count(0)
        zeros_count_first_gen_fish = first_gen_fish.count(0)
        fish = tick_fish_clock(first_gen=False, fish=fish)
        fish += spawn_new_baby_fish(
            first_gen=False, num_baby_fish=zeros_count_first_gen_fish
        )
        first_gen_fish = tick_fish_clock(first_gen=True, fish=first_gen_fish)
        first_gen_fish += spawn_new_baby_fish(
            first_gen=True, num_baby_fish=zeros_count_fish
        )
    print(f"all fish after {i+1} days: ", len(fish) + len(first_gen_fish))


def day6_test_b():
    fname = "days/6/test_input.txt"
    istate = read_input_data(fname)
    total = 0
    for j, fish in enumerate(istate[0:1]):
        fish = [fish]
        print("Initial state: ", istate)
        first_gen_fish = []
        for i in range(120):
            zeros_count_fish = fish.count(0)
            zeros_count_first_gen_fish = first_gen_fish.count(0)
            fish = tick_fish_clock(first_gen=False, fish=fish)
            fish += spawn_new_baby_fish(
                first_gen=False, num_baby_fish=zeros_count_first_gen_fish
            )
            first_gen_fish = tick_fish_clock(first_gen=True, fish=first_gen_fish)
            first_gen_fish += spawn_new_baby_fish(
                first_gen=True, num_baby_fish=zeros_count_fish
            )
            print(
                f"After {i:3},{len(fish) + len(first_gen_fish) }  days:",
                # fish + first_gen_fish,
            )
        print(
            f"{istate[j]} initial fish there are after {i+1} days: ",
            len(fish) + len(first_gen_fish),
        )
        total += len(fish) + len(first_gen_fish)

    print(f"All fish after {i+1} days: ", total)


def day6_b():
    fname = "days/6/input.txt"
    istate = read_input_data(fname)
    total = 0
    for j, fish in enumerate(istate[0]):
        fish = [fish]
        print("Initial state: ", istate)
        first_gen_fish = []
        for i in range(18):
            zeros_count_fish = fish.count(0)
            zeros_count_first_gen_fish = first_gen_fish.count(0)
            fish = tick_fish_clock(first_gen=False, fish=fish)
            fish += spawn_new_baby_fish(
                first_gen=False, num_baby_fish=zeros_count_first_gen_fish
            )
            first_gen_fish = tick_fish_clock(first_gen=True, fish=first_gen_fish)
            first_gen_fish += spawn_new_baby_fish(
                first_gen=True, num_baby_fish=zeros_count_fish
            )
            print(f"After {i:3}  days:", fish + first_gen_fish)
        print(
            f"{istate[j]} initial fish there are after {i+1} days: ",
            len(fish) + len(first_gen_fish),
        )
        total += len(fish) + len(first_gen_fish)

    print(f"All fish after {i+1} days: ", total)


# day6_test_a()
# day6_a()
day6_test_b()
