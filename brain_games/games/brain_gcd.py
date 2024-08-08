import random
from math import gcd

RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    RANDOM_NUM_FROM = 1
    RANDOM_NUM_TO = 20
    num_one = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    num_two = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    correct_answer = gcd(num_one, num_two)
    question = f'{num_one} {num_two}'
    return question, str(correct_answer)
