import random

# Константы для генерации случайных чисел
RANDOM_NUM_FROM = 1
RANDOM_NUM_TO = 20
# Константы для длины прогрессии
LENGTH_MIN = 5
LENGTH_MAX = 10

RULE = "What number is missing in the progression?"


def get_question_and_answer():
    start = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    step = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    length = random.randint(LENGTH_MIN, LENGTH_MAX)
    progression = [str(start + i * step) for i in range(length)]
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    return ' '.join(progression), correct_answer
