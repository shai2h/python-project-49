from brain_games.utils import get_random_number
from brain_games.scripts.run_games import run_game
from brain_games.cli import welcome_user


def gcd(num_one, num_two):
    while num_two != 0:
        num_one, num_two = num_two, num_one % num_two
    return num_one


def question_gcd():
    num_one = get_random_number(1, 20)
    num_two = get_random_number(1, 20)
    correct_answer = gcd(num_one, num_two)
    return num_one, num_two, correct_answer

def brain_gcd():
    name = welcome_user()
    rules = 'Find the greatest common divisor of given numbers.'
    run_game(question_gcd, rules, name)
