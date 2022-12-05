with open("input", 'r') as input_file:
    is_tree = [[c == '#' for c in line.strip()] for line in input_file.readlines()]

n_rows = len(is_tree)
width = len(is_tree[0])

# Right, Down
slope = (1, 2)

hit = [is_tree[y][x] for x,y in [(u*slope[0]%width, u*slope[1]) for u in range(n_rows//slope[1])]]
print(hit.count(True))



