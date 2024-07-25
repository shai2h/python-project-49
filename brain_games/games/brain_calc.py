import random


def generate_calc_question():
    operation = ['+', '-', '*']
    random_num_one = random.randint(0, 20)
    random_num_two = random.randint(0, 20)
    random_operation = random.choice(operation)
    expression = f'{random_num_one} {random_operation} {random_num_two}'
    return expression, eval(expression)
