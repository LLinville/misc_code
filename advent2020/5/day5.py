with open("input", 'r') as input_file:
    print(max([int(''.join(['1' if c=='B' else '0' for c in line[:7]]),2) * 8 + int(''.join(['1' if c=='R' else '0' for c in line[7:]]),2)for line in input_file.readlines()]))

print(max([int(''.join(['1' if c in ['B', 'R'] else '0' for c in line]), 2) for line in input_file.readlines()]))