with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines() if len(line) > 1]

reductions = ["()", "<>", "[]", "{}"]

closings = [r[1] for r in reductions]

scores = {
    '': 0,
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

total_score = 0
for line in lines:
    while True:
        reduced = line
        for reduction in reductions:
            reduced = reduced.replace(reduction, "")
        if reduced == line:
            break
        else:
            line = reduced
    closing_locations = [
        line.find(closing) for closing in closings
    ]
    closing_location = [l for l in closing_locations if l >= 0]
    closing_char = line[min(closing_location)] if closing_location else ''
    total_score += scores[closing_char]
    print(f"{line} {'invalid' if len(set(line) & set(closings)) else 'valid'}")
    print(f"Closing char: {line[min(closing_location)] if closing_location else ''}\n")

print(total_score)

# total_score = 0
# for line in lines:
#     closing_locations = [
#         line.find(closing) for closing in closings
#     ]
#     closing_location = [l for l in closing_locations if l >= 0]
#     print(f"Closing char: {closing_location}")
#     print(f"{line} {'invalid' if len(set(line) & set(closings)) else 'valid'}")
