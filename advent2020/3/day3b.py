with open("input", 'r') as input_file:
    is_tree = [[c == '#' for c in line.strip()] for line in input_file.readlines()]

# Right, Down
slope = (1, 2)

hit = [is_tree[y][x] for x,y in [(u*slope[0]%len(is_tree[0]), u*slope[1]) for u in range(len(is_tree)//slope[1])]]
print(hit.count(True))



