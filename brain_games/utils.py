import random


def get_random_number(start, end):
    return random.randint(start, end)


def get_user_answer():
    return input('Your answer: ').lower().strip()


def is_game_complete(target_score, target_score_needed):
    return target_score < target_score_needed


def gcd(num_one, num_two):
    while num_one != num_two:
        if num_one > num_two:
            num_one = num_one - num_two
        else:
            num_two = num_two - num_one
    return (num_one)
