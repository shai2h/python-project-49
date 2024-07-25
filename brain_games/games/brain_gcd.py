import random


def generate_gcd_question():
    def gcd(num_one, num_two):
        while num_two != 0:
            num_one, num_two = num_two, num_one % num_two
        return num_one

    num_one = random.randint(1, 20)
    num_two = random.randint(1, 20)
    correct_answer = gcd(num_one, num_two)
    return num_one, num_two, correct_answer
