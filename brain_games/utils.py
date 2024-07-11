import random


def get_random_number(start, end):
    return random.randint(start, end)


def get_user_answer():
    return input('Your answer: ').lower().strip()


def is_game_complete(target_score, target_score_needed):
    return target_score < target_score_needed


def gcd(num_one, num_two):
    while num_two != 0:
        num_one, num_two = num_two, num_one % num_two
    return num_one
