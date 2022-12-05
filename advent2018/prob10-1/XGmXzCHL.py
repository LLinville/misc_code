import re


def find_area_coordinates_span(coordinate_data):
    width = find_coordinates_width(coordinate_data)
    height = find_coordinates_height(coordinate_data)
    return width * height


def find_coordinates_height(coordinate_data):
    min_y = min(data[1] for data in coordinate_data)
    max_y = max(data[1] for data in coordinate_data)
    return max_y - min_y


def find_coordinates_width(coordinate_data):
    min_x = min(data[0] for data in coordinate_data)
    max_x = max(data[0] for data in coordinate_data)
    return max_x - min_x


def move_coordinate_points(coordinate_data):
    new_data_dict = {(x + x_velocity, y + y_velocity): (x_velocity, y_velocity) for
                     (x, y), (x_velocity, y_velocity) in coordinate_data.items()}

    return new_data_dict


def reverse_coordinate_points(coordinate_data):
    new_data_dict = {(x - x_velocity, y - y_velocity): (x_velocity, y_velocity) for
                     (x, y), (x_velocity, y_velocity) in coordinate_data.items()}
    return new_data_dict


def parse_data(coordinates_lines):
    data_dict = {}
    for num, line in enumerate(coordinates_lines):
        __, x, y, __, x_velocity, y_velocity, __ = re.split("< |<|> |>|, ", line.strip())
        x = int(x)
        y = int(y)
        x_velocity = int(x_velocity)
        y_velocity = int(y_velocity)
        data_dict[x, y] = (x_velocity, y_velocity)
    return data_dict


def print_coordinate_data(coordinate_data):
    min_x = min(data[0] for data in coordinate_data)
    max_x = max(data[0] for data in coordinate_data)
    min_y = min(data[1] for data in coordinate_data)
    max_y = max(data[1] for data in coordinate_data)

    for y_val in range(min_y, max_y+1):
        for x_val in range(min_x, max_x+1):
            if (x_val, y_val) in coordinate_data:
                print("#", end="")
            else:
                print(" ", end="")
        print()


def print_and_move_coordinates_until_done(coordinate_data, seconds):
    input_val = ""
    while not input_val:
        print("\n\n\n\n\n\n")
        seconds += 1
        print(seconds)
        coordinate_data = move_coordinate_points(coordinate_data)
        print_coordinate_data(coordinate_data)
        input_val = input()


def main():
    tolerance = 50
    seconds = 0

    with open("10-TheStarsAlign-Input.txt") as input_file:
        coordinates_lines = input_file.readlines()
    coordinate_data_dict = parse_data(coordinates_lines)

    with open("10-TheStarsAlign-Input.txt") as input_file:
        coordinates_lines = input_file.readlines()
    coordinate_data = parse_data(coordinates_lines)
    for i in range(10054):
        test_a = {(x + x_velocity, y + y_velocity): (x_velocity, y_velocity) for
                  (x, y), (x_velocity, y_velocity) in coordinate_data.items()}
        coordinate_data = test_a
    # coordinate_data = {(x + x_velocity * 10054, y + y_velocity * 10054): (x_velocity, y_velocity) for
#                       (x, y), (x_velocity, y_velocity) in coordinate_data.items()}
    for y_val in range(107, 120):
        for x_val in range(180, 300):
            if (x_val, y_val) in coordinate_data:
                print("#", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    main()