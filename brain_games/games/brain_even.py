import random
from brain_games.utils import is_even

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    RANDOM_NUM_FROM = 0
    RANDOM_NUM_TO = 20
    random_num = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    if is_even(random_num):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_num, correct_answer
