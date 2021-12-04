import re

with open("input", 'r') as input_file:
    lines = input_file.readlines()

children = {}
for line in lines:
    color = re.findall("(\w+ \w+) bags contain", line)[0]
    children[color] = {color for quantity, color in re.findall("(\d+) (\w+ \w+) bags?", line)}

def get_all_child_colors(color):
    return children[color].union(*[get_all_child_colors(child_color) for child_color in children[color]])

print(len([True for color in children.keys() if 'shiny gold' in get_all_child_colors(color)]))



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