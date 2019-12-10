# state = [True if char == '#' else False for char in "..#..####.##.####...#....#######..#.#..#..#.#.#####.######..#.#.#.#..##.###.#....####.#.#....#.#####"]
state = "..#..####.##.####...#....#######..#.#..#..#.#.#####.######..#.#.#.#..##.###.#....####.#.#....#.#####"
rules_string = '''#.##. => .
#.#.. => .
###.# => .
..#.# => .
....# => .
.#### => .
##.## => #
###.. => #
.###. => #
...#. => .
..... => .
##..# => .
.#.#. => #
.#.## => #
##.#. => .
##... => .
##### => #
#...# => .
..##. => .
..### => .
.#... => #
.##.# => .
#.... => .
.#..# => .
.##.. => #
...## => #
#.### => .
#..#. => .
..#.. => #
#.#.# => #
####. => #
#..## => .'''

# state = [True if char == '#' else False for char in "...#..#.#..##......###...###..........."]
# state = "..#..####.##.####...#....#######..#.#..#..#.#.#####.######..#.#.#.#..##.###.#....####.#.#....#.#####"
# rules_string = '''...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #'''

# rule_kernels = [[True if char == '#' else False for char in line[:5]] for line in rules_string.split('\n')]
# rule_results = [True if line[9] == '#' else False for line in rules_string.split('\n')]
rule_kernels = [line[:5] for line in rules_string.split('\n')]
rule_results = [line[9] for line in rules_string.split('\n')]

padding_length = 0
padded_state = '.' * padding_length + state + '.' * padding_length
result_state = padded_state

for iteration in range(20):

    state_chunks = [result_state[i:i+5] for i in range(0, len(result_state) - 4)]

    result_state = '..'
    for state_chunk in state_chunks:
        matching_rule_index = rule_kernels.index(state_chunk)
        result_state += rule_results[matching_rule_index]
    result_state += '..'
    print(result_state)
print(sum([index for index in range(len(result_state)) if result_state[index] == '#']))

