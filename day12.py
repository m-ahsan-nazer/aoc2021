from typing import List, Tuple, Dict
from pprint import pprint
import copy
import itertools as it


def read_input_data(fname: str) -> List[Tuple[str, str]]:
    input_data = []
    with open(fname, "r") as f:
        for line in f:
            key, value = line.strip().strip("\n").split("-")
            input_data.append((key, value))

    return input_data


def process_data(input_data: List[Tuple[str, str]]) -> Dict:
    data = dict.fromkeys([item[0] for item in input_data], None)
    for key in data:
        data[key] = []
    for key, value in input_data:
        # don't want infinite loops
        if value != "start":
            data[key].append(value)

    return data


def create_tree(data: Dict) -> Dict:
    assert "start" in data
    tree = {}


def replace_key_with_value(key: str, data: Dict) -> Dict:
    # value = data.get(key, None)
    # path = ""
    # if value == "end":
    #     return "end"
    # if value:
    #     path += replace_key_with_value(value, data)

    # return path
    data_copy = copy.deepcopy(data)
    for key in data:
        list_value = data_copy[key]
        # paths = [data.get(path) for path in paths]
        dict_value = dict.fromkeys(list_value)
        for k in dict_value:
            dict_value[k] = data_copy.get(k)
        data_copy[key] = dict_value

    return data_copy


def find_paths(data: Dict) -> Dict:
    paths = [["start"]]
    cur_len_paths = len(paths)
    while True:
        last_entry = paths[-1]
        additions = []
        print(paths)
        for key in last_entry:
            if key == "end":
                additions.append(key)
            if data.get(key):
                additions = data.get(key)
        if additions:
            paths.append(additions)
        if len(paths) == cur_len_paths:
            break
        cur_len_paths = len(paths)
    return paths


def traverse_path(data: Dict) -> List[str]:
    paths = []
    path = []
    path.append("start")
    key = data.get("start")
    while True:
        path.append(key)
        replace_key_with_value(key, data)


def day12_test_a():
    fname = "days/12/test_input.txt"
    input_data = read_input_data(fname)
    data = process_data(input_data)
    pprint(input_data)
    pprint(data)
    # path = replace_key_with_value("start", data)
    # pprint(("path", path))
    # pprint(("data", data))
    paths = find_paths(data)
    pprint(paths)


def day12_a():
    fname = "days/12/input.txt"
    input_data = read_input_data(fname)


def day12_test_b():
    fname = "days/12/test_input.txt"
    input_data = read_input_data(fname)


def day12_b():
    fname = "days/12/input.txt"
    input_data = read_input_data(fname)


if __name__ == "__main__":
    day12_test_a()
    # day12_a()
    # day12_test_b()
    # day12_b()
