# Define a class to represent a player on the leaderboard
class Player:
    """Defined a class to represent a player on the leader board, as this gets developed will make this pull from all users who have bet"""
    def _init_(self, name, predictions):
        self.name = name
        self.predictions = predictions
        self.score = 0

# Create a dictionary to store the game results
game_results = {
    "game1": (3, 1),
    "game2": (0, 0),
    "game3": (2, 2),
}

# Create a list to store the players on the leaderboard
leaderboard = []

# Define a function to add a new player to the leaderboard
def add_player(name, predictions):
    player = Player(name, predictions)
    leaderboard.append(player)

# Define a function to update a player's score
def update_score(player, game_id):
    prediction = player.predictions[game_id] # Get the player's prediction for this game
    result = game_results[game_id] # Get the actual result for this game
    score = abs(prediction[0] - result[0]) + abs(prediction[1] - result[1]) # Calculate the player's score based on how close their prediction was to the actual result
    player.score += score # Update the player's score

def display_leaderboard():
    """Function to display the leaderboard"""
    leaderboard.sort(key=lambda x: x.score)     # Sort the players by score in ascending order
    for player in leaderboard: # Loop through each player on the leaderboard
        print(f"{player.name}: {player.score}") # Print the player's name and score
        for game_id, result in game_results.items(): # Loop through each game
            print(f"{game_id}: {player.predictions[game_id]}") # Print the player's prediction for this game

        # Print a separator
        print("-" * 20)

# Test Code
add_player("Alice", {"game1": (3, 1), "game2": (0, 0), "game3": (2, 2)})