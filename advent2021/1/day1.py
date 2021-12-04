with open('input.txt', 'r') as input_file:
    depths = [int(line.strip()) for line in input_file.readlines()]

increasing = 0
for i in range(1, len(depths)):
    print(f"{depths[i]} > {depths[i-1]} ?")
    if depths[i] > depths[i-1]:
        increasing += 1

print(increasing)