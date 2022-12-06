from data_reader import get_data
# from game_logic import choose_team

# """
#     {'_id': ObjectId('638d43a372ca0bb8d4a800a6'), 
#     'name': 'Benjamin Funk', 
#     'email': 'bfunk1.personal@gmail.com', 
#     'bets': [{'home_team': 'Japan', 'away_team': 'Croatia', 'home_score': '2', 'away_score': '2', 'penalties': 'True'},
#             {'home_team': 'Korea', 'away_team': 'US', 'home_score': '2', 'away_score': '1', 'penalties': 'False'}]}
# """


def get_scores(bet):
    total_points = 0
    
    if bet == None:
        return total_points
    # GET PREDICTED
    pred_home_score, pred_away_score = int(bet['home_score']), int(bet['away_score'])

    pred_diff = pred_home_score - pred_away_score
    if pred_diff == 0:
        pred_penalties = True
    else:
        pred_penalties = False

    # TODO: Get actual scores from API
    response_data = get_data()
    data = response_data["response"]
    for g in data:
        home_act = g["teams"]["home"]["name"]
        away_act = g["teams"]["away"]["name"]
        if home_act == bet['home_team'] and away_act == bet['away_team']:
            actual_home_score = g['score']['fulltime']['home']
            actual_away_score = g['score']['fulltime']['away']
            break

    act_diff = actual_home_score - actual_away_score
    if act_diff == 0:
        actual_penalties = True
    else:
        actual_penalties = False

    # QUERY FOR PENALITIES

    # if there is a draw and penalties are predicted
    if pred_penalties == actual_penalties:
        total_points += 1

    # got predicted score right
    if pred_away_score == actual_away_score and pred_home_score == actual_home_score:
        total_points += 1

    # got winner right
    if (pred_diff > 0 and act_diff > 0) or (pred_diff < 0 and act_diff < 0):
        total_points += 1


    # return total_points
    return total_points, pred_home_score, pred_away_score, pred_diff, pred_penalties, actual_home_score, actual_away_score, act_diff


