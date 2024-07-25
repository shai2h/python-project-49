import random


def generate_prime_question():
    random_num = random.randint(1, 20)
    if random_num < 2:
        return random_num, 'no'
    for i in range(2, int(random_num ** 0.5) + 1):
        if random_num % i == 0:
            return random_num, 'no'
    return random_num, 'yes'
