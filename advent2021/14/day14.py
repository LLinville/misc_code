with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines() if len(line) > 1]

sequence = lines[0]
rules = {
    (r := line.split(" -> "))[0]: r[1] for line in lines[1:]
}

for i in range(10):
    out = []
    for pair_index in range(len(sequence) - 1):
        pair = sequence[pair_index:pair_index+2]
        out.append(pair[0])
        if pair in rules.keys():
            out.append(rules[pair])
    out.append(sequence[-1])
    sequence = ''.join(out)
all_symbols = set(sequence)
count_by_symbol = {
    symbol: len([c for c in sequence if c == symbol])
        for symbol in all_symbols
}
print(len(sequence))
print(f"{(mx:=max(count_by_symbol.values()))} - {(mn:=min(count_by_symbol.values()))} = {mx-mn}")