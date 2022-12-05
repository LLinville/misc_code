def part_one(their_throw, your_response):
    round_points = 0
    if their_throw == 'A': # Rock
        if your_response == 'X': # Rock (+1)
            round_points += 4 # Draw (+3)
        if your_response == 'Y': # Paper (+2)
            round_points += 8 # Win (+6)
        if your_response == 'Z': # Scissors (+3)
            round_points += 3 # Loss (+0)

    elif their_throw == 'B': # Paper
        if your_response == 'X': # Rock (+1)
            round_points += 1 # Loss (+0)
        if your_response == 'Y': # Paper (+2)
            round_points += 5 # Draw (+3)
        if your_response == 'Z': # Scissors (+3)
            round_points += 9 # Win (+6)    

    elif their_throw == 'C': # Scissors
        if your_response == 'X': # Rock (+1)
            round_points += 7 # Win (+6)
        if your_response == 'Y': # Paper (+2)
            round_points += 2 # Loss (+0)
        if your_response == 'Z': # Scissors (+3)
            round_points += 6 # Draw (+3)
    return round_points


def part_two(their_throw, your_response):
    round_points = 0
    if their_throw == 'A': # Rock
        if your_response == 'X': # Need to lose (+0)
            round_points += 3 # Scissors (+3)
        if your_response == 'Y': # Need to draw (+3)
            round_points += 4 # Rock (+1)
        if your_response == 'Z': # Need to win (+6)
            round_points += 8 # Paper (+2)

    elif their_throw == 'B': # Paper
        if your_response == 'X': # Need to lose (+0)
            round_points += 1 # Rock (+1)
        if your_response == 'Y': # Need to draw (+3)
            round_points += 5 # Paper (+2)
        if your_response == 'Z': # Need to win (+6)
            round_points += 9 # Scissors (+3)  

    elif their_throw == 'C': # Scissors
        if your_response == 'X': # Need to lose (+0)
            round_points += 2 # Paper (+2)
        if your_response == 'Y': # Need to draw (+3)
            round_points += 6 # Scissors (+3)
        if your_response == 'Z': # Need to win (+6)
            round_points += 7 # Rock (+1)
    return round_points

part_one_score = 0
part_two_score = 0

with open('input.txt') as input_data:
    input_data = [line.strip() for line in input_data.readlines()]

    for round in input_data:
        part_one_score += part_one(round[0], round[2])
        part_two_score += part_two(round[0], round[2])

print(part_one_score)
print(part_two_score)