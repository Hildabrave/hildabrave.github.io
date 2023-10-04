import random

# roll dice until the max
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll


while True:
    players = input("Enter the number of players(2-4):")
    if players.isdigit():
        players = int(players)  # convert string to int
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
# initial the score for all the players
players_scores = [0 for _ in range(players)]
# _ can also use "i" but we do not care about this in this case
while max(players_scores) < max_score:
    for player_idx in range(players):
        print("\n------------------Player", player_idx + 1, "turn has just started!---------------\n")
        print("Your total score is", players_scores[player_idx])
        current_score = 0

        while True:

            should_roll = input("would you like to roll (y)?")
            if should_roll.lower() != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a :", value)

            print("Your score is ", current_score)

        players_scores[player_idx] += current_score
        print("Your total score is :", players_scores[player_idx])

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number", winning_idx+1, "is the winner of a score of:", max_score)