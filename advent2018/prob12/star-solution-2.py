def parse_data(plant_data):
    initial_state = plant_data[0].split()[-1]
    dict_of_rules = {}
    for line in plant_data[2:]:
        pot_layout, __, result = line.split()
        dict_of_rules[pot_layout] = result
    return initial_state, dict_of_rules


def spread_plants(current_state, dict_of_rules, initial_index):
    minimum_number_to_append_left = 5
    for num in range(1, 6):
        if set(current_state[:num]) == {"."}:
            minimum_number_to_append_left -= 1
        else:
            break

    minimum_number_to_append_right = 5
    for num in range(1, 6):
        if set(current_state[-num:]) == {"."}:
            minimum_number_to_append_right -= 1
        else:
            break

    initial_index -= minimum_number_to_append_left
    left_append_state = "." * minimum_number_to_append_left
    right_append_state = "." * minimum_number_to_append_right
    current_state = left_append_state + current_state + right_append_state

    new_state = current_state[0:4]
    for num, plant in enumerate(current_state[4:-4], 4):
        plant_state = current_state[num-2 : num+3]
        plant_result = dict_of_rules[plant_state]
        new_state += plant_result
    new_state += current_state[-4:]
    return new_state, initial_index


def get_index_and_state_over_time(initial_state, dict_of_rules, length_of_time=20):
    current_state = initial_state
    current_index = 0
    set_of_all_states = set()
    current_time = 0

    for __ in range(length_of_time):
        current_state, current_index = spread_plants(current_state, dict_of_rules, current_index)
    return current_state, current_index


def sum_plant_values(final_state, index):
    final_sum = 0
    for num, value in enumerate(final_state, index):
        if value == "#":
            final_sum += num
    return final_sum


# def extrapolate_and_sum_plant_values(first_repetition_state, initial_repetition_index, first_repetition_index):
#


def main():
    with open("12-SubterraneanSustainability-Input.txt") as input_file:
        plant_data = input_file.readlines()
    initial_state, dict_of_rules = parse_data(plant_data)

    final_state, final_index = get_index_and_state_over_time(initial_state, dict_of_rules)
    print(final_state, final_index)

    final_sum = sum_plant_values(final_state, final_index)
    print(final_sum)

    # final_state, final_index = get_index_and_state_over_time(initial_state, dict_of_rules, length_of_time=50000000000)
    # print(final_state, final_index)


if __name__ == "__main__":
    main()