import collections
import matplotlib
import numpy as np


Point = collections.namedtuple("Point", ["x","y","dx","dy"])

with open("input.txt") as input_text:
    lines = input_text.readlines()

points = []
for line in lines:
    x = int(line[10:16])
    y = int(line[18:24])
    dx = int(line[36:38])
    dy = int(line[40:42])
    points.append(Point(x, y, dx, dy))


