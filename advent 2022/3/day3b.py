from itertools import islice

def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

def char_score(char):
    o = ord(char)
    return o - 96 if o >= 97 else o - 64 + 26

with open('input.txt') as input_file:
    lines = input_file.readlines()
lines = [line.strip() for line in lines]

total_score = 0
groups = chunk(lines, 3)
for group in groups:
    shared = set(group[0]) & set(group[1]) & set(group[2])
    total_score += char_score(next(iter(shared)))


print(total_score)
