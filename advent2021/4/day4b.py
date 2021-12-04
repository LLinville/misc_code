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
remaining_boards = set({i for i in range(len(lines)//5)})
for call in calls:
    called.add(call)
    for winning_set, b_i in winning_sets.items():
        if winning_set.issubset(called):
            remaining_boards.discard(b_i)
            print(f"Board {b_i} won after {call} was called. {len(remaining_boards)} remaining")
        if len(remaining_boards) == 1:
            last_board = [i for i in remaining_boards][0]
        if len(remaining_boards) == 0:
            unmarked_sum = sum([
                sum([item for item in lines[last_board*5 + r] if item not in called]) for r in range(5)
            ])
            print(f"board {last_board} was last after {call} was called. Score: {unmarked_sum * int(call)}")
            quit()



