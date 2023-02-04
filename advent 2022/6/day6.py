def all_unique(chars):
    for i in range(len(chars)):
        if chars[i] in chars[:i] + chars[i+1:]:
            return False
    return True

filename = 'input.txt'
with open(filename) as input_file:
    lines = input_file.readlines()

line = lines[0]
for i in range(len(line) - 14):
    if all_unique(line[i:i+14]):
        print(i+4)
        break