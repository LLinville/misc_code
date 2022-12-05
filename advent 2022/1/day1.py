

with open('input.txt') as input_file:
    lines = input_file.readlines()

calorie_totals = []
total = 0
for line in lines:
    if line.strip():
        total += int(line.strip())
    else:
        calorie_totals.append(total)
        total = 0

print(sum(sorted(calorie_totals)[-3:]))