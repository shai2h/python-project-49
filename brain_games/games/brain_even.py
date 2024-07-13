from brain_games.cli import welcome_user
from brain_games.utils import (
    get_random_number,
    get_user_answer,
    is_game_complete
)


def brain_even(name):

    target_score = 0
    target_score_needed = 3
    yes_answer = 'yes'
    no_answer = 'no'

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while is_game_complete(target_score, target_score_needed):
        random_num = get_random_number(0, 20)
        print(f'Question: {random_num}')
        user_answer = get_user_answer()

        if random_num % 2 == 0:
            correct_answer = yes_answer
        else:
            correct_answer = no_answer

        if user_answer == correct_answer:
            print('Correct!')
            target_score += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(.\n"
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break

    if target_score == target_score_needed:
        print(f'Congratulations, {name}!')


def main():
    name = welcome_user()
    brain_even(name)


if __name__ == '__main__':
    main()
