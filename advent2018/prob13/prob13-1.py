
carts = dict()

with open("input.txt") as input_file:
    input_lines = input_file.readlines()

for y_index, line in enumerate(input_lines):
    for x_index, character in enumerate(line):
        if character in "NSEW":

            carts[(x_index, y_index)] = ({
                'heading': ['N', 'E', 'S', 'W'][['^', '>', 'v', '<'].index(character)],
                'next_turn': 'L'
            })
#
# track_char = [[input_lines[y][x] for y in range(len(input_lines[0]))] for x in range(len(input_lines))]


cart_locations = sorted(carts.keys())

for sorted_cart in cart_locations:
    cart = carts[sorted_cart]
    track_char = input_lines[sorted_cart[0]][sorted_cart[1]]
    heading = cart['heading']
    next_turn = cart['next_turn']
    if track_char in "-|":
        target_heading = heading
    elif track_char == "\\":
        target_heading = "WSEN"["NESW".index(heading)]
    elif track_char == "/":
        target_heading = "ENWS"["NESW".index(heading)]
    elif track_char == "#":
        # Intersection
        if next_turn == "L":
            target_heading = "WNES"["NESW".index(heading)]
            next_turn = "C"
        elif next_turn == "C":
            target_heading = heading
            next_turn = "R"
        elif next_turn == "R":
            target_heading = "ESWN"["NESW".index(heading)]
            next_turn = "L"

    next_position = None
    if heading == "N":
        next_position = (sorted_cart[0], sorted_cart[1] - 1)
    elif heading == "E":
        next_position = (sorted_cart[0] + 1, sorted_cart[1])
    elif heading == "S":
        next_position = (sorted_cart[0], sorted_cart[1] + 1)
    elif heading == "W":
        next_position = (sorted_cart[0] - 1, sorted_cart[1])
    # Check for collision


    # Step cart forward






for y_index, line in enumerate(input_lines):
    for x_index, character in enumerate(line):
        cart = carts[(x_index, y_index)]
        track_char = input_lines[x_index][y_index]




