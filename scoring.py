from data_reader import get_data
from game_logic import choose_team


def get_team_1():
    team = input("input team 1 >>> ")
    user_team_1 = ' '.join(x.capitalize() for x in team.split())
    if user_team_1 in ("Usa", "USa", "United States", "US", "Us", "United States Of America"):
        user_team_1 = "USA"
    games = choose_team(user_team_1)
    if games == []:
        raise ValueError(
            'This team is not on the roster. Check your spelling! (Capitalization is not required.)')
    print(f'Here are the games and scores for {user_team_1}: {games}.')
    return games, user_team_1


def choose_game():
    games, user_team_1 = get_team_1()
    team = input("input team 2 >>> ").capitalize()
    user_team_2 = ' '.join(x.capitalize() for x in team.split())
    if user_team_2 in ("Usa", "USa", "United States", "US", "Us", "United States Of America"):
        user_team_2 = "USA"
    for game in games:
        if user_team_2 in game:
            return game, user_team_1, user_team_2
    raise ValueError(
        'This team is not on the roster. Check your spelling! (Capitalization is not required.)')


def create_score_dict():
    game, user_team_1, user_team_2 = choose_game()
    score_1 = int(
        input(f"how many points will {user_team_1} end up with? >>> "))
    score_2 = int(
        input(f"how many points will {user_team_2} end up with? >>> "))
    if score_1 > score_2:
        winner = user_team_1
    elif score_1 < score_2:
        winner = user_team_2
    elif score_1 == score_2:
        team = input(
            'Predicting a draw means predicting a penatlies round. Which team will win? >>> ')
        winner = ' '.join(x.capitalize() for x in team.split())
        if winner in ("Usa", "USa", "United States", "US", "Us", "United States Of America"):
            winner = "USA"
    prediction = {user_team_1: score_1, user_team_2: score_2}
    return game, prediction, winner


def get_winner():
    real_game, pred_game, pred_winner = create_score_dict()
    user_team_1, user_team_2 = pred_game.keys()
    response_data = get_data()
    data = response_data["response"]
    for g in data:
        home_team = g["teams"]["home"]["name"]
        away_team = g["teams"]["away"]["name"]
        home_win = g["teams"]["home"]["winner"]
        away_win = g["teams"]["away"]["winner"]
        if user_team_1 == home_team and user_team_2 == away_team:
            if home_win == True:
                winner = home_team
            elif away_win == True:
                winner = away_team
            else:
                winner = None
        elif user_team_1 == away_team and user_team_2 == home_team:
            if home_win == True:
                winner = home_team
            elif away_win == True:
                winner = away_team
            else:
                winner = None
    return real_game, pred_game, winner, pred_winner


def get_penalties():
    real_game, pred_game, real_winner, pred_winner = get_winner()
    team_1, team_2 = real_game.keys()
    if real_game[team_1] == real_game[team_2] and real_game[team_1] != None and real_game[team_2] != None:
        penalties = True
    else:
        penalties = False
    return real_game, pred_game, real_winner, pred_winner, penalties


def compare_scores():
    points = 0
    real_game, pred_game, real_winner, pred_winner, penalties = get_penalties()
    team_1, team_2 = real_game.keys()
    if penalties == True:
        points += 1
    if real_game[team_1] == pred_game[team_1] and real_game[team_2] == pred_game[team_2]:
        points += 1
    if pred_winner == real_winner:
        points += 1
    return real_game, pred_game, real_winner, pred_winner, penalties, points


# print(create_score_dict())
# print(get_winner())
# compare_scores()
print(compare_scores())
