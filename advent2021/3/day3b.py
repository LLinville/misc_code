def digit_sieve(lines, most_common=True):
    for d in range(len(lines[0])):
        # print(lines)
        ones = [line for line in lines if line[d] == '1']
        zeroes = [line for line in lines if line[d] == '0']
        if most_common:
            lines = zeroes if len(ones) < len(zeroes) else ones
        else:
            lines = ones if len(ones) < len(zeroes) else zeroes

        if len(lines) == 1:
            return lines[0]


with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

oxy = int(digit_sieve(lines, True), 2)
co2 = int(digit_sieve(lines, False), 2)
print(f"oxygen={oxy}, co2={co2}, rating={oxy*co2}")
