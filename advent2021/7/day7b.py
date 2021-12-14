
with open('input.txt', 'r') as input_file:
    positions = [int(i) for i in input_file.readline().strip().split(',')]

width = max(positions)

cost_sums = [sum([
        abs(pos - p) * (abs(pos - p)+1) //2 for pos in positions]
    ) for p in range(width + 1)]

for i, c in enumerate(cost_sums):
    print(f"{i}: {c}")
print(min(cost_sums))
mean = sum(positions)/len(positions)
median_cost = sum([abs(pos - mean) * (abs(pos - mean)+1) //2 for pos in positions])
print(f"median: {mean}, cost: {median_cost}")
