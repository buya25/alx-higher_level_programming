#!/usr/bin/python3
def get_highest_score_name(scores_dict):
    """
    gets the best value from a dictionary (greatest integer)
    """
    winner_name = None
    highest_score = float('-inf')  # Initialize with negative infinity
    if isinstance(scores_dict, dict):
        for name, score in scores_dict.items():
            if isinstance(score, int) and score > highest_score:
                highest_score = score
                winner_name = name
    return winner_name
