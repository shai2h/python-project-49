

def get_user_answer():
    return input('Your answer: ').lower().strip()


def is_game_complete(target_score, target_score_needed):
    return target_score < target_score_needed
