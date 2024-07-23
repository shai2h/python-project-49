from brain_games.utils import get_random_number
from brain_games.scripts.run_games import run_game
from brain_games.cli import welcome_user


def is_prime():
    random_num = get_random_number(1, 20)
    correct_answer = ''
    if random_num < 2:
        correct_answer = 'no'
    for i in range(2, int(random_num ** 0.5) + 1):
        if random_num % i == 0:
            correct_answer = 'no'
    correct_answer = 'yes'
    return random_num, correct_answer


def brain_prime():
    name = welcome_user()
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(is_prime, rules, name)
