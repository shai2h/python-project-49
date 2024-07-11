from brain_games.utils import (
    get_random_number,
    is_game_complete,
    get_user_answer
)
from brain_games.cli import welcome_user


def brain_progression(name):
    target_score = 0
    target_score_needed = 3
    print("What number is missing in the progression?")
    while is_game_complete(target_score, target_score_needed):
        nums_amount = get_random_number(5, 20)

        nums_list = [str(i) for i in range(1, nums_amount, 2)]

        nums = len(nums_list)
        random = get_random_number(0, nums - 1)

        right_num = nums_list[random]
        nums_list[random] = '..'

        print(f'Question: {nums_list}')
        user_answer = get_user_answer()

        if user_answer != right_num:
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
            target_score += 1
    if target_score == target_score_needed:
        print(f'Congratulations, {name}!')


def main():
    name = welcome_user()
    brain_progression(name)


if __name__ == '__main__':
    main()
