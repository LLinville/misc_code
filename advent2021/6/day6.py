with open('input.txt', 'r') as input_file:
    fish = [int(i) for i in input_file.readline().strip().split(',')]

count_by_age = {
    i: len([f for f in fish if f==i]) for i in range(9)
}

print(fish)

for d in range(80):
    new_count_by_age = {i:0 for i in range(9)}
    for age in [0, 1, 2, 3, 4, 5, 7]: # calculate 6 and 8 separate
        new_count_by_age[age] = new_count_by_age[age + 1]
    new_count_by_age[6] = new_count_by_age[0]
    new_count_by_age[8] = new_count_by_age[0]
    count_by_age = new_count_by_age

print(len(fish))