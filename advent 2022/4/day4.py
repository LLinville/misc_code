
def overlaps(outer, inner):
    return min(inner) >= min(outer) and max(inner) <= max(outer)


with open('input.txt') as input_file:
    lines = input_file.readlines()
lines = [line.strip() for line in lines]

total = 0
for line in lines:
    left_text, right_text = line.split(',')
    left_range = [int(text) for text in left_text.split('-')]
    right_range = [int(text) for text in right_text.split('-')]
    if overlaps(left_range, right_range) or overlaps(right_range, left_range):
        total += 1

print(total)