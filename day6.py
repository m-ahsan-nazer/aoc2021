from typing import Dict, List


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
    for i in range(256):
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


def get_rep_from_num(pos: int, num: int) -> Dict:
    """
    e.g
    {0:1, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
    """
    rep = {}
    for i in range(9):
        rep[i] = 0
    rep[pos] = num
    return rep


def get_additions_for_rep(rep: Dict) -> Dict:
    additions = {}
    for i in range(0, 8):
        additions[i] = rep[i + 1]
    additions[8] = rep[0]
    additions[6] += rep[0]
    return additions


def update_rep(rep: Dict) -> Dict:
    additions = get_additions_for_rep(rep)
    for key in rep:
        rep[key] = additions[key]


def get_rep_after_n_days(rep: Dict, num: int) -> Dict:
    for i in range(num):
        update_rep(rep)
    return rep


def day6_test_b():
    fname = "days/6/test_input.txt"
    istate = read_input_data(fname)
    istate_rep = get_rep_from_num(0, 0)
    for i in istate:
        rep = get_rep_from_num(i, 1)
        for j in rep:
            istate_rep[j] += rep[j]
    print("istate: ", istate)
    print("istate rep: ", istate_rep)
    # rep = get_rep_from_num(0, 1)
    # print(rep)
    # num_days = 18
    # num_days = 80
    num_days = 256
    rep = get_rep_after_n_days(istate_rep, num_days)
    print(f"After {num_days} ", sum(rep.values()))
    print(rep.values())


def day6_b():
    fname = "days/6/input.txt"
    istate = read_input_data(fname)
    istate_rep = get_rep_from_num(0, 0)
    for i in istate:
        rep = get_rep_from_num(i, 1)
        for j in rep:
            istate_rep[j] += rep[j]
    # num_days = 18
    # num_days = 80
    num_days = 256
    rep = get_rep_after_n_days(istate_rep, num_days)
    print(f"After {num_days} ", sum(rep.values()))
    print(rep.values())


# day6_test_a()
# day6_a()
# day6_test_b()
day6_b()
