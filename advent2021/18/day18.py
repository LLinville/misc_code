with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines() if len(line) > 1]


def parse(line):
    depths = []
    values = []
    depth = 0
    for char in line:
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char in '0123456789':
            depths.append(depth)
            values.append(int(char))
    return depths, values

def reduce(values, depths):
    print(f"\nvalues: {values}\ndepths:  {depths}")
    for i, (depth, value) in enumerate(zip(depths, values)):

        if depth > 4 and i < len(depths) - 1 and depths[i + 1] == depth:
            print("Explode")
            if i - 1 >= 0:
                values[i - 1] += value
            if i + 2 < len(values):
                values[i + 2] += values[i + 1]

            values = values[:i] + [0] + values[i + 2:]
            depths = depths[:i] + [depth - 1] + depths[i + 2:]
            break
        elif value > 9:
            print("Split")
            values = values[:i] + [value // 2, value // 2 + value % 2] + values[i + 1:]
            depths = depths[:i] + [depth + 1, depth + 1] + depths[i + 1:]
            break
    else:
        print('done')
        print(f"\nvalues: {values}\ndepths:  {depths}")
        return values, depths

def add(v1, d1, v2, d2):
    depths = [d+1 for d in d1] + [d+1 for d in d2]
    values = v1+v2
    return reduce(values, depths)

print(add(*parse(lines[0]), *parse(lines[1])))

