import re

'''
Split into grid where each box adds six division lines
With n boxes, this is (2n+1)(2n+1)(2n+1), which is O(n^3) in memory and time
'''

'''

'''
def intersection_boxes(x1, x2, y1, y2, z1, z2):




pattern = re.compile(r"o[nf]+ x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)")

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines() if len(line) > 1]

lines = [[int(i) for i in pattern.match(line).groups()] for line in lines]

boxes = []
for x1, x2, y1, y2, z1, z2 in lines:
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    z1, z2 = min(z1, z2), max(z1, z2)
    new_boxes = []

    for box in boxes:
        if intersects()
