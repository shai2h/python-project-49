from brain_games.cli import welcome_user
import random
from brain_games.utils import get_random_number, is_game_complete


def question_calc():
    operation = ['+', '-', '*']
    random_num_one = get_random_number(0, 20)
    random_num_two = get_random_number(0, 20)
    random_operation = random.choice(operation)
    expression = f'{random_num_one} {random_operation} {random_num_two}'
    return expression, eval(expression)


def brain_calc(name):
    target_score = 0
    target_score_needed = 3
    print("What is the result of the expression?")
    while is_game_complete(target_score, target_score_needed):
        expression, answer_expression = question_calc()
        print(f'Question: {expression}')
        user_answer = input('Your answer: ')
        try:
            if int(user_answer) == answer_expression:
                target_score += 1
                print('Correct!')
            else:
                print(
                    f"'{user_answer}' is wrong answer ;(.\n"
                    f"Correct answer was '{answer_expression}'."
                )
                print(f"Let's try again, {name}!")
                break
        except ValueError:
            print(
                f"'{user_answer}' is wrong answer ;(.\n"
                f"Correct answer was '{answer_expression}'."
            )
            break
    if target_score == target_score_needed:
        print(f'Congratulations, {name}!')


def main():
    name = welcome_user()
    brain_calc(name)


if __name__ == '__main__':
    main()
