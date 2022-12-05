with open("input", 'r') as input_file:
    lines = input_file.readlines()

n_valid = 0
for line in lines:
    bounds, letter, password = line.split(" ")
    lower_bound, upper_bound = [int(v) for v in bounds.split("-")]
    letter = letter[0]
    count = password.count(letter)
    if lower_bound <= count <= upper_bound:
        n_valid += 1
print(n_valid)