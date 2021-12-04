with open('input.txt', 'r') as input_file:
    depths = [int(line.strip()) for line in input_file.readlines()]

window_sums = [depths[i] + depths[i+1] + depths[i+2] for i in range(len(depths)-2)]

increasing = 0
for i in range(1, len(window_sums)):
    if window_sums[i] > window_sums[i-1]:
        increasing += 1

print(increasing)
