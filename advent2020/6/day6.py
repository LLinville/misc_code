with open("input", 'r') as input_file:
    groups = input_file.read().split('\n\n')

print(sum([len(set(group)) for group in groups]))