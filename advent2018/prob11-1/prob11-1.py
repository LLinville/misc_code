import matplotlib.pyplot as pyplot


def fuel_level(x, y, serial=6303):
    print(x, y)
    fuel = ((x + 10) * y + serial) * (x + 10)
    return (fuel // 100) % 10 - 5


def neighbor_sum(data, x, y):
    return sum([sum([data[x+dx][y+dy] for dy in [-1,0,1]]) for dx in [-1,0,1]])

fuel_levels = [[fuel_level(x, y) for y in range(1, 301)] for x in range(1, 301)]

max_level = 0
max_coordinate = None
neighbor_sums = [[neighbor_sum(fuel_levels, x, y) for y in range(1, 299)] for x in range(1, 299)]
for x in range(1, 299):
    for y in range(1, 299):
        sum_of_neighbors = neighbor_sum(fuel_levels, x, y)
        if sum_of_neighbors > max_level:
            max_level = sum_of_neighbors
            max_coordinate = (x, y)

print(max_level, max_coordinate)
pyplot.imshow(fuel_levels)
#pyplot.imshow(neighbor_sums)
pyplot.show()
