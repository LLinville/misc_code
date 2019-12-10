from collections import defaultdict
def visit_node(node, dependencies, is_node_visited):
    if is_node_visited[node]:
        return

    unvisited_dependencies = [dependency for dependency in dependencies[node] if not is_node_visited[dependency]]

    for dependency in sorted(unvisited_dependencies):
        visit_node(dependency, dependencies, is_node_visited)
    is_node_visited[node] = True
    print(node)



with open("input.txt", "r+") as input_file:
    directed_pairs = [(line[5], line[36]) for line in input_file.readlines()]

prerequisites = dict()
for dependency, dependent in directed_pairs:
    if dependency not in prerequisites.keys():
        prerequisites[dependency] = []
    if dependent not in prerequisites.keys():
        prerequisites[dependent] = []
    prerequisites[dependent].append(dependency)

is_node_visited = dict()
for node, dependent in directed_pairs:
    is_node_visited[node] = False
    is_node_visited[dependent] = False

root_queue = set()
for prerequisite in prerequisites.keys():
    root_queue.add(prerequisite)
    root_queue.update(prerequisites[prerequisite])

root_queue = sorted(list(root_queue))
while not len(root_queue) == 0:
    visit_node(root_queue[0], prerequisites, is_node_visited)
    root_queue = root_queue[1:]
