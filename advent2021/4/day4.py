with open('input.txt', 'r') as input_file:
    lines = [line.strip().split(',') for line in input_file.readlines() if len(line) > 1]

calls = [int(item) for item in lines[0]]
del lines[0]
lines = [[int(item) for item in line[0].replace('  ', ' ').split(' ')] for line in lines]

winning_sets = {}
for b_i in range(len(lines)//5):
    for r in range(5):
        winning_sets[frozenset(
            lines[b_i*5+r]
        )] = b_i
        winning_sets[frozenset(lines[b_i * 5 + c][r] for c in range(5))] = b_i

called = set({})
for call in calls:
    called.add(call)
    for winning_set, b_i in winning_sets.items():
        if winning_set.issubset(called):
            unmarked_sum = sum([
                sum([item for item in lines[b_i*5 + r] if item not in called]) for r in range(5)
            ])
            print(f"board {b_i} had {winning_set} after {call} was called. Score: {unmarked_sum * int(call)}")
            quit()



