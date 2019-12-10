with open("input.txt") as infile:
    wire1 = infile.readline().split(',')
    wire2 = infile.readline().split(',')

dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
wire1_offsets = [
    (dirs[text[0]][0] * int(text[1:]), dirs[text[0]][1] * int(text[1:])) for text in wire1
]

wire2_offsets = [
    (dirs[text[0]][0] * int(text[1:]), dirs[text[0]][1] * int(text[1:])) for text in wire1
]

prev_node = (0,0)
wire1_nodes = set()
wire2_nodes = set()
for offset in wire1_offsets:
    prev_node = (prev_node[0] + offset[0], prev_node[1] + offset[1])
    wire1_nodes.add(prev_node)

prev_node = (0,0)
for offset in wire2_offsets:
    prev_node = (prev_node[0] + offset[0], prev_node[1] + offset[1])
    wire2_nodes.add(prev_node)

dists = [abs(node[0]) + abs(node[1]) for node in wire1_nodes.intersection(wire2_nodes)]
print(min(dists))
