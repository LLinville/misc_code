with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]
commands = [line.split(' ') for line in lines]
hpos = 0
dpos = 0

for command in commands:
    dir = command[0]
    mag = int(command[1])
    if dir == 'forward':
        hpos += mag
    elif dir == 'up':
        dpos -= mag
    elif dir == 'down':
        dpos += mag
print(dpos*hpos)