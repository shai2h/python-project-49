import random


def generate_even_question():
    yes_answer = 'yes'
    no_answer = 'no'
    random_num = random.randint(0, 20)
    if random_num % 2 == 0:
        correct_answer = yes_answer
    else:
        correct_answer = no_answer
    return random_num, correct_answer
