from typing import List, Dict, Tuple, NewType
from pprint import pprint
import copy


def read_data_input(fname: str) -> Tuple[str, Dict, int]:
    """
    iea: image enhancement algorithm
    """
    input_image = {}
    iea = ""
    dim: int = None
    with open(fname, "r") as f:
        line = f.readline()
        line = line.strip().strip("\n")
        iea = line
        # read empty line
        f.readline()
        # now read input image
        line_num = f.tell()
        line = f.readline()
        dim = len(line.strip().strip("\n"))
        f.seek(line_num)
        y = 0
        for line in f:
            line = line.strip().strip("\n")
            for x, c in enumerate(line):
                input_image[x, y] = c
            y += 1

    return (iea, input_image, dim)


def map_coords_value_to_pixel(
    output_pixel_coord: Tuple[int, int], iea: str, input_image: Dict, dim: int
) -> str:
    input_pixels = ""
    x, y = output_pixel_coord
    for j in [y - 1, y, y + 1]:
        for i in [x - 1, x, x + 1]:
            pixel_value = input_image.get((i, j), ".")
            input_pixels += pixel_value

    input_pixels = input_pixels.replace("#", "1")
    input_pixels = input_pixels.replace(".", "0")
    input_pixels_decimal_value = int(input_pixels, 2)
    return iea[input_pixels_decimal_value]


def get_output_image(
    iea: str, input_image: Dict, dim: int
) -> Tuple[Dict[Tuple[int, int], str], int]:
    output_image = {}
    input_image_with_boundary = {}
    # for (x, y) in input_image:
    #     pixel_value = map_coords_value_to_pixel((x, y), iea, input_image, dim)
    #     output_image[x, y] = pixel_value
    new_dim = dim + 4
    for y in range(-2, dim + 2):
        for x in range(-2, dim + 2):
            input_image_with_boundary[x + 2, y + 2] = input_image.get((x, y), ".")
    # pprint(input_image_with_boundary.keys())
    # print_image(input_image_with_boundary, new_dim)
    for (x, y) in input_image_with_boundary:
        pixel_value = map_coords_value_to_pixel(
            (x, y), iea, input_image_with_boundary, new_dim
        )
        output_image[x, y] = pixel_value
    return (output_image, new_dim)


def print_image(image: Dict[Tuple[int, int], str], dim: int):
    for y in range(dim):
        for x in range(dim):
            print(image[x, y], end="")
        print()
    print()


def day20_test_a():
    fname = "days/20/test_input.txt"
    iea, input_image, dim = read_data_input(fname)
    # pixel_value = map_coords_value_to_pixel((2, 2), iea, input_image, dim)
    # print(iea[0], iea[1], iea[2], iea[34])
    # for i, c in enumerate(iea):
    # print(i, c)
    # print(pixel_value)
    print_image(input_image, dim)
    image, new_dim = get_output_image(iea, input_image, dim)
    print_image(image, new_dim)
    image, new_dim = get_output_image(iea, image, new_dim)
    print_image(image, new_dim)
    print("# count: ", list(image.values()).count("#"))


def day20_a():
    fname = "days/20/input.txt"
    iea, input_image, dim = read_data_input(fname)
    print(iea)
    print("dim: ", dim)
    print("# count: ", list(input_image.values()).count("#"))
    print_image(input_image, dim)
    image, new_dim = get_output_image(iea, input_image, dim)
    print_image(image, new_dim)
    image, new_dim = get_output_image(iea, image, new_dim)
    print_image(image, new_dim)
    print("# count: ", list(image.values()).count("#"))


def day20_test_b():
    fname = "days/20/test_input.txt"


def day20_b():
    fname = "days/20/input.txt"


if __name__ == "__main__":
    # day20_test_a()
    day20_a()
    # day20_test_b()
    # day20_b()
