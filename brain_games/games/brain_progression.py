from brain_games.utils import (
    get_random_number,
    is_game_complete,
    get_user_answer
)
from brain_games.cli import welcome_user


def generate_progression():
    start = get_random_number(1, 10)
    step = get_random_number(1, 10)
    length = get_random_number(5, 10)
    progression = [str(start + i * step) for i in range(length)]
    return progression


def brain_progression(name):
    target_score = 0
    target_score_needed = 3
    print("What number is missing in the progression?")

    while is_game_complete(target_score, target_score_needed):
        progression = generate_progression()
        hidden_index = get_random_number(0, len(progression) - 1)
        correct_answer = progression[hidden_index]
        progression[hidden_index] = '..'

        print(f'Question: {" ".join(progression)}')
        user_answer = get_user_answer()

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
    brain_progression(name)


if __name__ == '__main__':
    main()
