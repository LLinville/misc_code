def get_instruction(operator):
    return lambda rs, i1, i2, d: [operator(rs, i1, i2) if i == d else r for i, r in enumerate(rs)]

instruction_maps = {
    # Lambda of registers, input1, input2
    "addr": lambda rs, i1, i2: rs[i1] + rs[i2],
    "addi": lambda rs, i1, i2: rs[i1] + i2,
    "mulr": lambda rs, i1, i2: rs[i1] * rs[i2],
    "muli": lambda rs, i1, i2: rs[i1] * i2,
    "banr": lambda rs, i1, i2: rs[i1] & rs[i2],
    "bani": lambda rs, i1, i2: rs[i1] & i2,
    "borr": lambda rs, i1, i2: rs[i1] | rs[i2],
    "bori": lambda rs, i1, i2: rs[i1] | i2,
    "setr": lambda rs, i1, i2: rs[i1],
    "seti": lambda rs, i1, i2: i1,
    "gtir": lambda rs, i1, i2: 1 if i1 > rs[i2] else 0,
    "gtri": lambda rs, i1, i2: 1 if rs[i1] > i2 else 0,
    "gtrr": lambda rs, i1, i2: 1 if rs[i1] > rs[i2] else 0,
    "eqir": lambda rs, i1, i2: 1 if i1 == rs[i2] else 0,
    "eqri": lambda rs, i1, i2: 1 if rs[i1] == i2 else 0,
    "eqrr": lambda rs, i1, i2: 1 if rs[i1] == rs[i2] else 0
}

print(get_instruction(lambda rs, i1, i2: rs[i1] + i2)([1,2,3,4], 3, 2, 0))