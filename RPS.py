# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    # Default move
    guess = "R"

    # Identify the bot based on move patterns
    if len(opponent_history) >= 6:
        # Check for Quincy's pattern (R -> P -> S -> R -> P -> S)
        if opponent_history[-6:] == ["R", "P", "S", "R", "P", "S"]:
            return "P"  # Quincy will play "R" next, so counter with "P"

    if len(opponent_history) > 2:
        # Kris repeats our last move, so we counter our own last move
        last_play = opponent_history[-1]
        counter_moves = {"R": "P", "P": "S", "S": "R"}
        guess = counter_moves[last_play]

    if len(opponent_history) > 10:
        # Abbey and Mrugesh analyze past moves, so we analyze the opponent’s frequency
        last_ten = opponent_history[-10:]
        most_common = max(set(last_ten), key=last_ten.count)

        # Counter the most common move
        counter_moves = {"R": "P", "P": "S", "S": "R"}
        guess = counter_moves[most_common]

    return guess


