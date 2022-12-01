import http.client
import json

def get_data():

    conn = http.client.HTTPSConnection("v3.football.api-sports.io")

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "95545dabcc3cfa791d8e0f5198ff71b1"
        }

    conn.request("GET", "/fixtures/?league=1&season=2022", headers=headers)
    res = conn.getresponse()
    data = res.read()
    response_text = data.decode("utf-8")
    response_data = json.loads(response_text)
    return response_data




def get_scores():
    response_data = get_data()
    scores = []
    fixture = 0
    while fixture < len(response_data["response"]):
        home_team = response_data["response"][fixture]["teams"]["home"]["name"]
        away_team = response_data["response"][fixture]["teams"]["away"]["name"]
        home_score = response_data["response"][fixture]["score"]["fulltime"]["home"]
        away_score = response_data["response"][fixture]["score"]["fulltime"]["away"]
        game_1 = (home_team, home_score, away_team, away_score)
        scores.append(game_1)
        fixture +=1
    return scores

goals_list = get_scores()
goals_dict = dict(enumerate(goals_list))

def clean_data():
    count = 0
    while count < len(goals_dict.keys()):
        for tup in goals_dict.values():
            element = {tup[0]: tup[1], tup[2]: tup[3]}
            goals_dict[count] = element
            count +=1
            
    return goals_dict
 





    