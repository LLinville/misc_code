with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines() if len(line) > 1]

sequence = lines[0]
rules = {
    (r := line.split(" -> "))[0]: r[1] for line in lines[1:]
}
all_symbols = set(sequence) | set(rules.values())

zeroes_by_pair = {
    symbol1 + symbol2: 0 for symbol1 in all_symbols for symbol2 in all_symbols
}

count_by_pair = {k:v for k,v in zeroes_by_pair.items()}
for pair in zip(sequence[:-1], sequence[1:]):
    count_by_pair[pair[0]+pair[1]] += 1

for i in range(40):
    new_count_by_pair = {k:v for k,v in zeroes_by_pair.items()}
    for pair, count in count_by_pair.items():
        if product := rules.get(pair):
            new_count_by_pair[pair[0]+product] += count
            new_count_by_pair[product+pair[1]] += count
    count_by_pair = new_count_by_pair

count_by_symbol = {
    symbol: sum([count for pair, count in count_by_pair.items() if pair[0] == symbol])
        for symbol in all_symbols
}

count_by_symbol[sequence[-1]] += 1
print(count_by_symbol)
print(f"{(mx:=max(count_by_symbol.values()))} - {(mn:=min(count_by_symbol.values()))} = {mx-mn}")