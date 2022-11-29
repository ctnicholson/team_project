import data_reader

scores_list = []
relevant_list = []

def choose_team(name):
    count = 0
    cleaned_score_dict = data_reader.clean_data()
    for i in cleaned_score_dict.values():
        scores_list.append(i)
    for x in scores_list:
        if name in x:
            relevant_list.append(x)
    return relevant_list
            
           
print(choose_team("Senegal"))

# Database stores list of dictionaries of User's bets

# Function that extracts score predictions from each data structure and compares them --> outputs how many points user gets