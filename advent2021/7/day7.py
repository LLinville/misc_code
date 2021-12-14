
with open('input.txt', 'r') as input_file:
    positions = [int(i) for i in input_file.readline().strip().split(',')]

width = max(positions)

cost_sums = [sum([abs(pos - p) for pos in positions]) for p in range(width + 1)]

median = sorted(positions)[len(positions)//2]
median_cost = sum([abs(median - pos) for pos in positions])
print(f"median: {median}, cost: {median_cost}")
