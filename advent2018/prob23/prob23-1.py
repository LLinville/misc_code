from collections import namedtuple
import re

Source = namedtuple("Source", ['x', 'y', 'z', 'r'])

input_line_pattern = "pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(-?\d+)"
input_line_matcher = re.compile(input_line_pattern)

with open("input.txt", "r+") as input_file:
    input_lines = input_file.read().splitlines()


sources = []

for line_index, line in enumerate(input_lines):
    print(line_index)
    match = input_line_matcher.match(line)
    ints = [int(match.group(i)) for i in range(1, 5)]
    sources.append(Source(*ints))

max_source = max(sources, key=lambda source: source.r)
proximal_sources = [source for source in sources if abs(source.x - max_source.x) + abs(source.y - max_source.y) + abs(source.z - max_source.z) <= max_source.r]
print(len(proximal_sources))
