import random
from math import gcd

RANDOM_NUM_FROM = 1
RANDOM_NUM_TO = 20

RULE = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num_one = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    num_two = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    correct_answer = gcd(num_one, num_two)
    question = f'{num_one} {num_two}'
    return question, str(correct_answer)
