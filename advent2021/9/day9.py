with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines() if len(line) > 1]

heights = [list([int(h) for h in line]) for line in lines]

adjacent_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

low_points = []

for x, row in enumerate(heights):
    for y, height in enumerate(row):
        for offset in adjacent_directions:
            if 0 <= x + offset[0] < len(heights) and 0 <= y + offset[1] < len(row) and height > heights[x+offset[0]][y+offset[1]]:
                break
        else:
            low_points.append((x,y))

print(sum([heights[x][y] for x,y in low_points]) + len(low_points))