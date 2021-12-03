from pprint import pprint
from typing import Tuple, List


def instructionToMove(instruction: str) -> Tuple[int, int]:
    dir, step_size = instruction.split(" ")
    step_size = int(step_size)
    if dir == "forward":
        return (step_size, 0)
    elif dir == "up":
        return (0, -step_size)
    elif dir == "down":
        return (0, step_size)


def getCoords(moves: List[Tuple[int, int]]) -> List[Tuple[int, int, int]]:
    # coords = [(x_coord_sub, y_coord_sub, y_coord_aim)]
    # sub_coords = coords[0][:2]
    # aim_coords = coords[0][2]
    coords = [(0, 0, 0)]
    for i, move in enumerate(moves):
        current_coords = coords[-1]
        forward, up_or_down = move
        if up_or_down:
            aim = current_coords[2] + up_or_down
            new_coords = (current_coords[0], current_coords[1], aim)
            coords.append(new_coords)
        elif forward:
            aim = current_coords[2]
            new_coords = (
                current_coords[0] + forward,
                current_coords[1] + forward * aim,
                aim,
            )
            coords.append(new_coords)

    return coords


def getNextCoord(
    move: Tuple[int, int], current_coord: Tuple[int, int, int]
) -> Tuple[int, int, int]:
    # coords = (x_coord_sub, y_coord_sub, y_coord_aim)
    # sub_coords = coords[:2]
    # aim_coord = coords[2]
    forward, up_or_down = move
    current_x_coord, current_y_coord, current_aim = current_coord
    if up_or_down:
        aim = current_aim + up_or_down
        next_coord = (current_x_coord, current_y_coord, aim)
    elif forward:
        aim = current_aim
        next_coord = (
            current_x_coord + forward,
            current_y_coord + forward * aim,
            aim,
        )
    return next_coord


def test():
    day2_test_input = """
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
        """
    moves = []
    for line in day2_test_input.strip().split("\n"):
        line = line.strip()
        moves.append(instructionToMove(line))

    x_moves, y_moves = zip(*moves)
    x_coords = [sum(x_moves[slice(0, i + 1)]) for i in range(len(x_moves))]
    y_coords = [sum(y_moves[slice(0, i + 1)]) for i in range(len(y_moves))]
    coords = list(zip(x_coords, y_coords))

    print(f"mutiplying final position {coords[-1][0]*coords[-1][1]}")


def testB():
    day2_test_input_b = """
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
        """
    moves = []
    for line in day2_test_input_b.strip().split("\n"):
        line = line.strip()
        moves.append(instructionToMove(line))

    coords = getCoords(moves)
    print(f"mutiplying final position {coords[-1][0]*coords[-1][1]}")
    pprint(coords)


def day2():
    fname = "days/2/input.txt"
    with open(fname, "r") as f:
        coord = (0, 0, 0)
        for line in f:
            line = line.strip()
            move = instructionToMove(line)
            coord = getNextCoord(move, coord)

    print(f"mutiplying final position {coord[0]*coord[1]}")
    pprint(coord)


test()
# testB()
# day2()
