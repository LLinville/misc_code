


def remaining_stack(symbols):
    stack = []
    for symobol in symbols:
        if not stack or symobol != closing_symbols[stack[-1]]:
            stack.append()




with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines() if len(line) > 1]

reductions = ["()", "<>", "[]", "{}"]

closing_symbols = {
    s[0]: s[1] for s in reductions
}

closings = [r[1] for r in reductions]

scores = {
    '': 0,
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

line_scores = []
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
    print(f"{line} {'invalid' if len(set(line) & set(closings)) else 'valid'}\n")
    if not len(set(line) & set(closings)):
        line_score = 0
        for c in line[::-1]:
            line_score *= 5
            line_score += scores[closing_symbols[c]]
        line_scores.append(line_score)
        print(f"line score: {line_score}")

    print(sorted(line_scores)[len(line_scores)//2])



# total_score = 0
# for line in lines:
#     closing_locations = [
#         line.find(closing) for closing in closings
#     ]
#     closing_location = [l for l in closing_locations if l >= 0]
#     print(f"Closing char: {closing_location}")
#     print(f"{line} {'invalid' if len(set(line) & set(closings)) else 'valid'}")
