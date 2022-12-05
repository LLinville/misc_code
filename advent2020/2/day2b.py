with open("input", 'r') as input_file:
    lines = input_file.readlines()

n_valid = 0
for line in lines:
    bounds, letter, password = line.split(" ")
    lower_bound, upper_bound = [int(v) for v in bounds.split("-")]
    letter = letter[0]
    l_match, u_match = password[lower_bound-1] == letter, password[upper_bound-1] == letter
    if l_match ^ u_match:
        n_valid += 1
print(n_valid)