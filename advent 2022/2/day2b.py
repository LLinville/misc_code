

def score(me, them):
    points_by_play = {
        'A': {
            'X': 4, # Rock ties Rock
            'Y': 1, # Rock loses Paper
            'Z': 7  # Rock wins Scissors
        },
        'B': {
            'X': 8, # Paper wins Rock
            'Y': 5, # Paper ties Paper
            'Z': 2  # Paper loses Scissors
        },
        'C': {
            'X': 3, # Scissors loses Rock
            'Y': 9, # Scissors wins Paper
            'Z': 6  # Scissors ties Scissors
        }
    }

    return points_by_play[me][them]


def score(me, them):
    score_by_choice = {
        'R': 1,
        'P': 2,
        'S': 3
    }

    score_by_outcome = {
        'L': 0,
        'T': 3,
        'W': 6
    }

    outcome_by_pairing = {
        'RR': 'T',
        'RP': 'L',
        'RS': 'W',
        'PR': 'W',
        'PP': 'T',
        'PS': 'L',
        'SR': 'L',
        'SP': 'W',
        'SS': 'T'
    }

    choice_by_input = {
        'A': 'R',
        'B': 'P',
        'C': 'S',
        'X': 'R',
        'Y': 'P',
        'Z': 'S'
    }

    me = choice_by_input[me]
    them = choice_by_input[them]
    outcome = outcome_by_pairing[me + them]
    return score_by_choice[me] + score_by_outcome[outcome]



with open('input.txt') as input_file:
    lines = input_file.readlines()

total_score = 0
for i, line in enumerate(lines):
    round_score = score(line[2], line[0])
    total_score += round_score
    print(f"Processed line {i+1} / {len(lines)} with score {round_score}")

print(total_score)

