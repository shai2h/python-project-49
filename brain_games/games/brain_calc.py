import random
from brain_games.utils import get_random_number
from brain_games.scripts.run_games import run_game
from brain_games.cli import welcome_user


def question_calc():
    operation = ['+', '-', '*']
    random_num_one = get_random_number(0, 20)
    random_num_two = get_random_number(0, 20)
    random_operation = random.choice(operation)
    expression = f'{random_num_one} {random_operation} {random_num_two}'
    return expression, eval(expression)


def brain_calc():
    name = welcome_user()
    rules = 'What is the result of the expression?'
    run_game(question_calc, rules, name)
