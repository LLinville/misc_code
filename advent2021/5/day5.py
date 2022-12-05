import re
from collections import defaultdict

pattern = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines() if len(line) > 1]

lines = [[int(i) for i in pattern.match(line).groups()] for line in lines]

containing_lines = defaultdict(lambda : [])

for l_i, line in enumerate(lines):
    if line[0] == line[2]:
        print(f"({line[0]},{line[1]}), ({line[2]},{line[3]}): vertical")
        a, b = min(line[1], line[3]), max(line[1], line[3])
        for y in range(a, b+1):
            containing_lines[(line[0], y)].append(l_i)

    elif line[1] == line[3]:
        print(f"({line[0]},{line[1]}), ({line[2]},{line[3]}): horizontal")
        a, b = min(line[0], line[2]), max(line[0], line[2])
        for x in range(a, b + 1):
            containing_lines[(x, line[1])].append(l_i)


overlaps = [key for key, value in containing_lines.items() if len(value) > 1]
print(len(overlaps))

# for x in range(10):
#     for y in range(10):
#         print(len(containing_lines[(y,x)]), end=" ")
#     print("")



