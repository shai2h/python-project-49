from brain_games.utils import (
    get_random_number,
    is_game_complete,
    get_user_answer
)
from brain_games.cli import welcome_user


def is_prime(random_num):
    if random_num < 2:
        return False
    for i in range(2, int(random_num ** 0.5) + 1):
        if random_num % i == 0:
            return False
    return True


def brain_prime(name):
    target_score = 0
    target_score_needed = 3
    yes_answer = 'yes'
    no_answer = 'no'

    while is_game_complete(target_score, target_score_needed):
        random_num = get_random_number(1, 20)
        prime_number = is_prime(random_num)
        print(f'Question: {random_num}')
        user_answer = get_user_answer()

        if (
            (user_answer == yes_answer and prime_number is True)
            or (user_answer == no_answer and prime_number is False)
        ):
            print('Correct!')
            target_score += 1
        else:
            print(f"Let's try again, {name}!")
        break
    if target_score == target_score_needed:
        print(f'Congratulations, {name}')


def main():
    name = welcome_user()
    brain_prime(name)


if __name__ == '__main__':
    main()
