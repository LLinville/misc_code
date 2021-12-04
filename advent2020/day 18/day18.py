import re

with open("input", 'r') as input_file:
    lines = input_file.readlines()

sum = 0
for line in lines:
    line = f"({line.strip()})"
    while re.match("[^\d]", line):
        old, new = line[:], ""
        while old != new:
            old = new
            new = re.sub("(\d+) \+ (\d+)",
                         lambda m: f"{int(m[1]) + int(m[2])}", line)
        line = new
        old, new = line[:], ""
        while old != new:
            old = new
            new = re.sub("(\d+) \* (\d+)",
                         lambda m: f"{int(m[1]) * int(m[2])}", line)
        line = new
        line = re.sub("\((\d+)\)", lambda m: f"{m[1]}", line)
    sum += int(line)
print(sum)

