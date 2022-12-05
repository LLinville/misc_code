
with open("input", "r") as input_file:
    entries = [int(entry) for entry in input_file.readlines()]

for e1 in entries:
    for e2 in entries:
        for e3 in entries:
            if e1 + e2 +e3 == 2020:
                print(f'{e1} + {e2} + {e3} = 2020\n{e1} * {e2} * {e3} = {e1*e2*e3}')
