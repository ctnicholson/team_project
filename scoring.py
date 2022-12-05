from data_reader import get_data
from game_logic import choose_team

"""
    {'_id': ObjectId('638d43a372ca0bb8d4a800a6'), 
    'name': 'Benjamin Funk', 
    'email': 'bfunk1.personal@gmail.com', 
    'bets': [{'home_team': 'Japan', 'away_team': 'Croatia', 'home_score': '2', 'away_score': '2', 'penalties': 'True'},
            {'home_team': 'Korea', 'away_team': 'US', 'home_score': '2', 'away_score': '1', 'penalties': 'False'}]}
"""

def get_scores(bets):
    total_points = 0

    for bet in bets:
        # GET PREDICTED
        pred_home_score, pred_away_score = bet['home_score'], bet['away_score']
        pred_penalties = bet['penalties'] #(BOOL)

        pred_diff = pred_home_score - pred_away_score

        # TODO: Get actual scores from API
        actual_home_score, actual_away_score = None 
        actual_penalties = None #(BOOL)

        home_diff = actual_home_score - actual_away_score

        # QUERY FOR PENALITIES

        # if there is a draw and penalties are predicted
        if pred_penalties == actual_penalties:
            points += 1
        
        # got predicted score right
        if pred_away_score == actual_away_score and pred_home_score == actual_home_score:
            points += 1
        
        # got winner right
        if pred_diff == home_diff:
            points += 1

    return total_points