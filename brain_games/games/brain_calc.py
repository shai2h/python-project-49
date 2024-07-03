from brain_games.cli import welcome_user
import random


def brain_calc(name):
    target_score = 0
    target_score_needed = 3
    operation = ['+', '-', '*']


    while target_score < target_score_needed:
        random_num_one = random.randint(1, 20)
        random_num_two = random.randint(1, 20)
        random_operation = random.choice(operation)
        
        expression = f'{random_num_one} {random_operation} {random_num_two}'
        answer_expression = eval(expression)
        
        print(f'Question: {expression}')
        user_answer = int(input('Your answer: '))

        if user_answer == answer_expression:
            target_score += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer_expression}'.")
            print(f"Let's try again, {name}!")
            break
    if target_score == target_score_needed:
        print(f'Congratulations, {name}')

    

def main():
    name = welcome_user()
    brain_calc(name)


if __name__ == '__main__':
    main()