import random
from brain_games.utils import is_prime

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    RANDOM_NUM_FROM = 1
    RANDOM_NUM_TO = 20
    random_num = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    if is_prime(random_num):
        answer = 'yes'
    else:
        answer = 'no'
    return random_num, answer
