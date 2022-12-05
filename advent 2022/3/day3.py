def char_score(char):
    o = ord(char)
    return o - 96 if o >= 97 else o - 64 + 26

with open('input.txt') as input_file:
    lines = input_file.readlines()
lines = [line.strip() for line in lines]

total_score = 0
for i, line in enumerate(lines):
    shared = set(line[:len(line)//2]) & set(line[len(line)//2:])
    score = char_score(next(iter(shared)))
    print(shared, score)
    total_score += score

print(total_score)
