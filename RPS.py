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
            return "P"  # Counter the expected next "R"

    if len(opponent_history) > 2:
        # Kris repeats the opponent's last move -> Play the counter
        if opponent_history[-1] == "R":
            guess = "P"
        elif opponent_history[-1] == "P":
            guess = "S"
        elif opponent_history[-1] == "S":
            guess = "R"

    if len(opponent_history) > 10:
        # Abbey and Mrugesh rely on past frequency -> Predict and counter
        last_ten = opponent_history[-10:]
        most_common = max(set(last_ten), key=last_ten.count)

        # Counter the most common move
        counter_moves = {"R": "P", "P": "S", "S": "R"}
        guess = counter_moves[most_common]

    return guess

