from typing import List, Dict, Tuple, NewType
from pprint import pprint


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
    for j in [y + 1, y, y - 1]:
        for i in [x - 1, x, x + 1]:
            pixel_value = input_image.get((i, j), ".")
            input_pixels += pixel_value

    input_pixels = input_pixels.replace("#", "1")
    input_pixels = input_pixels.replace(".", "0")
    input_pixels_decimal_value = int(input_pixels, 2)
    return iea[input_pixels_decimal_value - 1]


def get_output_image(
    iea: str, input_image: Dict, dim: int
) -> Dict[Tuple[int, int], str]:
    output_image = {}
    for (x, y) in input_image:
        pixel_value = map_coords_value_to_pixel((x, y), iea, input_image, dim)
        output_image[x, y] = pixel_value
    return output_image


def print_image(image: Dict[Tuple[int, int], str], dim: int):
    for y in range(dim):
        for x in range(dim):
            print(image[x, y], end="")
        print()
    print()


def day20_test_a():
    fname = "days/20/test_input.txt"
    iea, input_image, dim = read_data_input(fname)
    # pixel_value = map_coords_value_to_pixel((5, 10), iea, input_image, dim)
    # print(pixel_value)
    print_image(input_image, dim)
    image = get_output_image(iea, input_image, dim)
    print_image(image, dim)
    image = get_output_image(iea, image, dim)
    print_image(image, dim)


def day20_a():
    fname = "days/20/input.txt"


def day20_test_b():
    fname = "days/20/test_input.txt"


def day20_b():
    fname = "days/20/input.txt"


if __name__ == "__main__":
    day20_test_a()
    # day20_a()
    # day20_test_b()
    # day20_b()
