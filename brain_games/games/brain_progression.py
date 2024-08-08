import random

RULES = "What number is missing in the progression?"


def get_question_and_answer():
    RANDOM_NUM_FROM = 1
    RANDOM_NUM_TO = 20
    start = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    step = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    length = random.randint(5, 10)
    progression = [str(start + i * step) for i in range(length)]
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    return ' '.join(progression), correct_answer
