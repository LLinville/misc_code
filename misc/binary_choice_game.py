

def nonfinishing_games(symbols, win_conditions, n_ply=10):
    won = []
    ongoing = symbols[:]

    while len(ongoing[0]) <= n_ply:
        ongoing = [game + '0' for game in ongoing] + [game + '1' for game in ongoing]
        newly_won = []
        still_ongoing = []
        for game in ongoing:
            for target in win_conditions:
                if game.endswith(target):
                    newly_won.append(game)
                    # print(game)
                    break
            else:
                still_ongoing.append(game)
        ongoing = still_ongoing
        won += newly_won

    print(f"Found {len(ongoing)} ongoing games after {n_ply} ply")
    return ongoing


def repeat_length(to_search):
    for length in range(1, len(to_search) // 2):
        if to_search[:length] == to_search[length : length * 2]:
            return length
    return None


symbols = ['0', '1']
win_conditions = ['000', '101', '111']

ongoing_games = nonfinishing_games(symbols=symbols, win_conditions=win_conditions, n_ply=20)

repeat_lengths = [repeat_length(ongoing_game) for ongoing_game in ongoing_games]

print(max(repeat_lengths))