# TODO: This implementation is incorrect because it assumes only S/E moves. Counterexample:
'''
11666
61666
11666
16666
11111
'''


with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines() if len(line) > 1]
    risks = [[int(r) for r in line] for line in lines]

x_width = len(risks[0])
y_width = len(risks)

# Total risk of cells entered, including risk of just-entered (x,y) and excluding initial cell risk
min_risk = [[(0, None) for cell in row] for row in risks]


for x in range(1, x_width):
    min_risk[0][x] = (min_risk[0][x-1][0] + risks[0][x], 'W')

for y in range(1, y_width):
    min_risk[y][0] = (min_risk[y-1][0][0] + risks[y][0], 'N')


for y in range(1, y_width):
    for x in range(1, x_width):
        risk = risks[y][x]
        if min_risk[y-1][x][0] + risk < min_risk[y][x-1][0] + risk:
            min_risk[y][x] = (min_risk[y-1][x][0] + risk, 'N')
        else:
            min_risk[y][x] = (min_risk[y][x-1][0] + risk, 'W')

print(f"Minimum total risk to get to ({x_width},{y_width}): {min_risk[-1][-1][0]}")
for y in range(y_width):
    print(' '.join(['|' if d[1] == 'N' else '-' for d in min_risk[y]]))




# In SW-NE lines, progressing SE
# Each cell has a risk to pass through it, and a direction (N or W) of the lowest risk neighbor to come from
