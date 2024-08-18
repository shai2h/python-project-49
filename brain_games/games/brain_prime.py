import random

RANDOM_NUM_FROM = 1
RANDOM_NUM_TO = 20
RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_question_and_answer():
    random_num = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    if is_prime(random_num):
        answer = 'yes'
    else:
        answer = 'no'
    return random_num, answer
