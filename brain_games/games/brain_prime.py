from brain_games.utils import get_random_number
from brain_games.scripts.run_games import run_game
from brain_games.cli import welcome_user


def is_prime():
    random_num = get_random_number(1, 20)
    if random_num < 2:
        return random_num, 'no'
    for i in range(2, int(random_num ** 0.5) + 1):
        if random_num % i == 0:
            return random_num, 'no'
    return random_num, 'yes'


def brain_prime():
    name = welcome_user()
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(is_prime, rules, name)
