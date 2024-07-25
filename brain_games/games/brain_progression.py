import random


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 20)
    length = random.randint(2, 10)
    progression = [str(start + i * step) for i in range(length)]
    hidden_index = random.randint(0, len(progression) - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    return ' '.join(progression), correct_answer
