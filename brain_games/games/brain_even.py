from brain_games.utils import get_random_number
from brain_games.scripts.run_games import run_game
from brain_games.cli import welcome_user


def question_even():
    yes_answer = 'yes'
    no_answer = 'no'
    random_num = get_random_number(0, 20)
    if random_num % 2 == 0:
        correct_answer = yes_answer
    else:
        correct_answer = no_answer
    return random_num, correct_answer


def brain_even():
    name = welcome_user()
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(question_even, rules, name)
