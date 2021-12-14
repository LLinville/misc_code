import re
pattern = re.compile(r"([abcdefg]+ )|( [abcdefg]+)")

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines() if len(line) > 1]


digits_segments = [line.split('|')[1].strip().split(' ') for line in lines]
easy_digits_per_line = [
    len([
        digit for digit in digit_segments if len(digit) in [2, 3, 4, 7]
    ]) for digit_segments in digits_segments
]
print(sum(easy_digits_per_line))