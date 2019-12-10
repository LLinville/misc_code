def metadata_total(remaining_data):
    number_of_children = remaining_data.pop(0)
    metadata_length = remaining_data.pop(0)
    child_metadata_sum = 0
    for child_index in range(number_of_children):
        child_metadata_sum += metadata_total(remaining_data)
    return child_metadata_sum + sum([remaining_data.pop(0) for _ in range(metadata_length)])

with open("input.txt", "r+") as input_file:
    print(metadata_total([int(digits) for digits in input_file.readline().split(" ")]))
