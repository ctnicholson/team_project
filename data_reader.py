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

        # Create a tuple with the home team, home score, away team, and away score
        game = (home_team, home_score, away_team, away_score)
        scores.append(game)
        fixture += 1
    return scores


def clean_data():
    # Use the get_scores function to get the raw data
    raw_data = get_scores()

    # Initialize an empty list to store the clean data
    clean_data = []

    # Iterate over the items in the raw data
    for item in raw_data:
        item_array = []

        # Access the values in the tuple by their index, rather than by their key
        home_team_name = item[0]
        away_team_name = item[2]

        # Add the team names and scores to the item_array
        item_array.append(home_team_name)
        item_array.append(away_team_name)
        item_array.append((item[1], item[3]))

        # Check if the score is "None" and append the item_array to the clean_data list
        if (item[1], item[3]) == (None, None):
            clean_data.append(item_array)

    return clean_data

