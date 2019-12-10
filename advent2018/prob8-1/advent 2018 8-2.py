def metadata_total(remaining_data):
    number_of_children = remaining_data.pop(0)
    metadata_length = remaining_data.pop(0)

    child_values = [metadata_total(remaining_data) for _ in range(number_of_children)]
    current_metadata = [remaining_data.pop(0) for _ in range(metadata_length)]

    if number_of_children == 0:
        return sum(current_metadata)
    return sum([child_values[child_index-1] for child_index in current_metadata if 0 < child_index <= number_of_children])

with open("input.txt", "r+") as input_file:
    print(metadata_total([int(digits) for digits in input_file.readline().split(" ")]))
