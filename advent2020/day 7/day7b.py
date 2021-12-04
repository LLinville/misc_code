import re

with open("input", 'r') as input_file:
    lines = input_file.readlines()

children = {}
for line in lines:
    color = re.findall("(\w+ \w+) bags contain", line)[0]
    children[color] = re.findall("(\d+) (\w+ \w+) bags?", line)

def n_bags(color):
    return 1 + sum([
        int(quantity) * n_bags(child_color) for quantity, child_color in children[color]
    ])

print(n_bags('shiny gold') - 1)



# added = True
# while added:
#     added = False
#     for parent_color, child_colors in children:
#        for child_color in child_colors:
#            if child_color not in children[parent_color]:



# n_containments = 0
# while len(contained_in) != n_containments:
#     for container_color, content_list in children:
#         for quantity, content_color in content_list:
#             contained_in.add((content_color, container_color))


print(children)