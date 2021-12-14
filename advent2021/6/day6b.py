with open('input.txt', 'r') as input_file:
    fish = [int(i) for i in input_file.readline().strip().split(',')]

count_by_age = {
    i: len([f for f in fish if f==i]) for i in range(9)
}

for day in range(256):
    new_count_by_age = {i: 0 for i in range(9)}
    for age in [0, 1, 2, 3, 4, 5, 7]:  # calculate 6 and 8 separately
        new_count_by_age[age] = count_by_age[age + 1]
    new_count_by_age[6] = count_by_age[0] + count_by_age[7]
    new_count_by_age[8] = count_by_age[0]
    count_by_age = new_count_by_age

print(sum(count_by_age.values()))