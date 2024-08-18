import random

RANDOM_NUM_FROM = 0
RANDOM_NUM_TO = 20
RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_question_and_answer():
    random_num = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    correct_answer = 'yes' if is_even(random_num) else 'no'
    return random_num, correct_answer
