from brain_games.utils import get_random_number
from brain_games.scripts.run_games import run_game
from brain_games.cli import welcome_user


def generate_progression():
    start = get_random_number(1, 10)
    step = get_random_number(1, 10)
    length = get_random_number(5, 10)
    progression = [str(start + i * step) for i in range(length)]
    hidden_index = get_random_number(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, correct_answer


def brain_progression():
    name = welcome_user() 
    rules = "What number is missing in the progression?"
    run_game(generate_progression, rules, name)
