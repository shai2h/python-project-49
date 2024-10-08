import random

RANDOM_NUM_FROM = 0
RANDOM_NUM_TO = 20

RULE = 'What is the result of the expression?'


def get_question_and_answer():
    operation = ['+', '-', '*']
    random_num_one = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    random_num_two = random.randint(RANDOM_NUM_FROM, RANDOM_NUM_TO)
    random_operation = random.choice(operation)
    expression = f'{random_num_one} {random_operation} {random_num_two}'
    if random_operation == '+':
        expression_result = random_num_one + random_num_two
    elif random_operation == '-':
        expression_result = random_num_one - random_num_two
    elif random_operation == '*':
        expression_result = random_num_one * random_num_two
    return expression, str(expression_result)
