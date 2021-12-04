with open("output", "r") as file:
    lines = file.readlines()

ratings = {line[7:-7]: line[-4:-1] for line in lines}

sorted_names = sorted(ratings.keys(), key=lambda n: -1*float(ratings[n]))

with open("sorted_output.txt", "a") as output_file:
    for name in sorted_names:
        output_file.write(name + "\n")