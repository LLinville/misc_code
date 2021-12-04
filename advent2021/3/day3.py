with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
    to_sum = [[int(c)*2 -1 for c in line] for line in lines]

gamma = 0
epsilon = 0
length = len(lines[0])
for d in range(length):
    s = sum([line[d] for line in to_sum])
    if s > 0:
        gamma += 2**(length - d - 1)
    else:
        epsilon += 2**(length - d - 1)

print(f"g={gamma}, e={epsilon}, g*e={gamma*epsilon}")