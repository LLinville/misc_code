with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

line.split(",")
points = [[int(component) for component in line.split(',')] for line in lines]

connections = [
    {index for index, point in enumerate(points) if sum([point[i] - origin[i] for i in range(4)]) <= 3} for origin in points
]

cluster_parents = [None for p in points]
for index in range(len(points)):
     nearby_indexes = connections[index]
     ancestors = []
     for nearby_index in nearby_indexes:
         cluster_parent
     parent