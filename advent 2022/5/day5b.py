n_stacks = 3
max_size = 3
filename = 'input_example.txt'

n_stacks = 9
max_size = 8
filename = 'input.txt'

def read_initial(lines):
    stacks = [[] for i in range(n_stacks + 1)]
    for line in lines:
        for i in range(n_stacks + 1):
            if i==0:
                continue
            char = line[4 * i - 3]
            if char != ' ':
                stacks[i].append(char)

    return [stack[::-1] for stack in stacks]


with open(filename) as input_file:
    lines = input_file.readlines()

initial_lines = lines[:max_size]
stacks = read_initial(initial_lines)

for line in lines[max_size + 2:]:
    components = line.split(' ')
    quantity = int(components[1])
    source = int(components[3])
    destination = int(components[5])

    stacks[destination] += stacks[source][-1*quantity:]
    del stacks[source][-1*quantity:]

print(''.join([stack[-1] for stack in stacks if stack]))