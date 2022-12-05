import re
from collections import defaultdict
import collections

# Point = collections.namedtuple('Point',['x','y'])
#
# directions = {
#         (+1, +0): 'e',
#         (+1, -1): 'ne',
#         (+0, -1): 'n',
#         (-1, -1): 'nw',
#         (-1, +0): 'w',
#         (-1, +1): 'sw',
#         (+0, +1): 's',
#         (+1, +1): 'se',
#     }
#
# def direction(x1, y1, x2, y2):
#     direc = {
#         (+1, +0): 'e',
#         (+1, -1): 'ne',
#         (+0, -1): 'n',
#         (-1, -1): 'nw',
#         (-1, +0): 'w',
#         (-1, +1): 'sw',
#         (+0, +1): 's',
#         (+1, +1): 'se',
#     }
#
#     dx = x2 - x1
#     dy = y2 - y1
#     dx = dx/abs(dx) if dx != 0 else 0
#     dy = dy/abs(dx) if dy != 0 else 0
#     return directions[(dx, dy)]
#
# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.p1 = Point(x1, y1)
#         self.p2 = Point(x2, y2)
#         dx = x2 - x1
#         dy = y2 - y1
#         self.dx = dx / abs(dx) if dx != 0 else 0
#         self.dy = dy / abs(dx) if dy != 0 else 0
#         self.length = max(abs(dx), abs(dy))
#
#     def intersects(self, x, y):
#         if self.direction == 'horizontal':
#             return y == self.p1.y and self.p1.x <= x <= self.p2.x

if __name__ == "__main__":
    pattern = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

    with open('input.txt', 'r') as input_file:
        lines = [line.strip() for line in input_file.readlines() if len(line) > 1]

    lines = [[int(i) for i in pattern.match(line).groups()] for line in lines]
    lines = [l for l in lines if
                 l[0] == l[2] or
                 l[1] == l[3] or
                 abs(l[2]-l[0]) == abs(l[3]-l[1])
            ]

    containing_lines = defaultdict(lambda: [])

    for l_i, line in enumerate(lines):
        dx = line[2] - line[0]
        dy = line[3] - line[1]
        length = max(abs(dx), abs(dy))
        dx = dx / abs(dx) if dx else 0
        dy = dy / abs(dy) if dy else 0
        dx, dy = int(dx), int(dy)
        for p_i in range(int(length) + 1):
            containing_lines[(
                    line[0] + p_i * dx,
                    line[1] + p_i * dy
            )].append(l_i)

    overlaps = [key for key, value in containing_lines.items() if len(value) > 1]
    print(len(overlaps))

    # for x in range(1000):
    #     for y in range(1000):
    #         c = len(containing_lines[(y,x)])
    #         print(c if c else " ", end=" ")
    #     print("")



