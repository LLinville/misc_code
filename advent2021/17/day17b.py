target = ((128, 160), (-88, -142))
# target = ((20, 30), (-5, -10))

on_target = [] # Which (dx, dy) pairs eventually land in target range?
for _dx in range(0, 200):
    print(f"Considering dx={_dx}")
    for _dy in range(-200, 200):
        dx, dy = _dx, _dy
        x, y = 0, 0
        step_locations = []
        while x <= target[0][1] and y >= target[1][1]:
            step_locations.append((x,y))
            if target[0][0] <= x <= target[0][1] and target[1][1] <= y <= target[1][0]:
                print(step_locations)
                xy = (_dx, _dy)
                on_target.append(xy)
                break
            x += dx
            y += dy
            dx = 0 if dx == 0 else dx - 1
            dy -= 1

print(on_target)
print(len(on_target))
