with open('input.txt') as input_file:
    program_string = ''.join(input_file.readlines()).replace('\n','')

program_inputs = [5]
program_inputs = (i for i in program_inputs)

n_params = {1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3}

def debug(string):
    DEBUG = True and False
    if DEBUG:
        print(string)

def get_instruction(instruction):
    instruction_str = str(instruction)
    if len(instruction_str) in [1, 2]:
        opcode = int(instruction_str)
        modes = [0] * n_params[opcode]
    else:
        opcode = int(instruction_str[-2:])
        modes = instruction_str[:-2]
        modes = "0" * (n_params[opcode] - len(instruction_str) + 2) + modes
        modes = [int(m) for m in modes][::-1]
    return opcode, modes

def get(pos, mode):
    return tape[pos] if mode == 0 else pos

pos = 0
tape = [int(v) for v in program_string.split(',')]

while tape[pos] != 99:
    opcode, modes = get_instruction(tape[pos])
    debug("\nopcode " + str(opcode) + ", modes " + str(modes))
    debug(f'tape {pos}: {tape[pos:]}')
    debug(f'tape 223+: {tape[223:]}')
    if opcode == 1:
        debug(f"add [{tape[pos + 3]}] = {get(tape[pos + 1], modes[0])} + {get(tape[pos + 2], modes[1])}")
        tape[tape[pos + 3]] = get(tape[pos + 1], modes[0]) + get(tape[pos + 2], modes[1])
    elif opcode == 2:
        debug(f"mul [{tape[pos + 3]}] = {get(tape[pos + 1], modes[0])} * {get(tape[pos + 2], modes[1])}")
        tape[tape[pos + 3]] = get(tape[pos + 1], modes[0]) * get(tape[pos + 2], modes[1])
    elif opcode == 3:
        tape[tape[pos + 1]] = next(program_inputs)#input("input: ")
        debug("Inputting")
    elif opcode == 4:
        print('output at pos ' + str(pos) + ' : ' + str(get(tape[pos + 1], modes[0])))
    elif opcode == 5:
        if get(tape[pos + 1], modes[0]) != 0:
            pos = get(tape[pos + 2], modes[1])
            continue
    elif opcode == 6:
        if get(tape[pos + 1], modes[0]) == 0:
            pos = get(tape[pos + 2], modes[1])
            continue
    elif opcode == 7:
        if get(tape[pos + 1], modes[0]) < get(tape[pos + 2], modes[1]):
            tape[tape[pos + 3]] = 1
        else:
            tape[tape[pos + 3]] = 0
    elif opcode == 8:
        if get(tape[pos + 1], modes[0]) == get(tape[pos + 2], modes[1]):
            tape[tape[pos + 3]] = 1
        else:
            tape[tape[pos + 3]] = 0
    else:
        print("Unknown opcode " + str(opcode))
    pos += n_params[opcode] + 1


