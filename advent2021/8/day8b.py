'''
Segment numbering
 000
1   2
1   2
 333
4   5
4   5
 666
'''

# Deducing scrambling order
# from known mappings of overlapping subsets
all_segments = set([i for i in range(7)])

segments_per_digit = {
    0: [0, 1, 2, 4, 5, 6],
    1: [2, 5],
    2: [0, 2, 3, 4, 6],
    3: [0, 2, 3, 5, 6],
    4: [1, 2, 3, 5],
    5: [0, 1, 3, 5, 6],
    6: [0, 1, 3, 4, 5, 6],
    7: [0, 2, 5],
    8: [0, 1, 2, 3, 4, 5, 6],
    9: [0, 1, 2, 3, 5, 6]
}

digit_by_segments = {
    frozenset(v): k for k, v in segments_per_digit.items()
}

digits_by_length = {
    i: len([d for d in segments_per_digit.keys() if len(segments_per_digit[d]) == i])
    for i in range(2, 8)
}

forbidden_segments_by_length = {
    2: [0, 1, 3, 4, 6], # '1'
    3: [1, 3, 4, 6],    # '7'
    4: [0, 4, 6],       # '4'
    5: [],              # '2', '3', '5'
    6: [],              # '0', '6', '9'
    7: [],              # '8'
}

required_segments_by_length = {
    2: [2, 5],                  # '1'
    3: [0, 2, 5],               # '7'
    4: [1, 2, 3, 5],            # '4'
    5: [0, 3, 6],               # '2', '3', '5'
    6: [0, 1, 5, 6],            # '0', '6', '9'
    7: [0, 1, 2, 3, 4, 5, 6],   # '8'
}

forbidden_segments_by_length = {
    i: set(f) for i, f in forbidden_segments_by_length.items()
}

# allowed_segments_by_length = {
#     i: all_segments - forbidden_segments_by_length[i] for i in forbidden_segments_by_length.keys()
# }

def print_mapping_grid(allowed_mappings):
    print("   a b c d e f g")
    for i in range(7):
        print(f"{i}  {' '.join(['.' if s in allowed_mappings[i] else 'x' for s in 'abcdefg' ])}")
    print("\n")


def all_determined(allowed_mappings):
    for segment, mappings in allowed_mappings.items():
        if len(mappings) != 1:
            return False
    return True


def segment_mapping(shuffle_samples):
    all_options = set('abcdefg')
    allowed_mappings = {
        i: set(all_options)
        for i in range(7)
    }

    known_mappings = {
        i: None for i in range(7)
    }

    while not all_determined(allowed_mappings):
        for connected_wires in shuffle_samples:
            print_mapping_grid(allowed_mappings)
            for forbidden_segment in forbidden_segments_by_length[len(connected_wires)]:
                allowed_mappings[forbidden_segment] -= connected_wires

            for required_segment in required_segments_by_length[len(connected_wires)]:
                allowed_mappings[required_segment] -= all_options - connected_wires

        for segment in range(7):
            if len(allowed_mappings[segment]) == 1: # We know one for sure. Remove segment from other wires
                wire = list(allowed_mappings[segment])[0]
                for i in set(range(7)) - {segment}:
                    allowed_mappings[i] -= {wire}
    print_mapping_grid(allowed_mappings)
    return {
        list(allowed_mappings[i])[0]: i for i in range(7)
    }



with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines() if len(line) > 1]


digits_wires = [line.split('|')[0].strip().split(' ') for line in lines]
outputs_wires = [line.split('|')[1].strip().split(' ') for line in lines]


segments_by_wire = segment_mapping([set(m) for m in digits_wires[0]])
# segments_per_input_digit =
for digits_wires in outputs_wires:
    digits = [
        digit_by_segments[frozenset([segments_by_wire[w] for w in digit_wires])]
        for digit_wires in digits_wires
    ]
    print(digits)


# Given ab,
# for each forbidden segment mapping f, remove {a,b} from allowed_mappings[f]







