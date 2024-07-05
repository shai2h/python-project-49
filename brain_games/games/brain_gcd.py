from brain_games.utils import get_random_number, is_game_complete, gcd
from brain_games.cli import welcome_user




def brain_gcd(name):
    target_score = 0
    target_score_needed = 3
    while is_game_complete(target_score, target_score_needed):
        num_one = get_random_number()
        num_two = get_random_number()
        correct_answer = gcd(num_one, num_two)

        print(f'Question: {num_one} {num_two}')
        user_answer = input("Your answer: ")
        if user_answer == correct_answer:
            target_score += 1
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if target_score == target_score_needed:
        print(f'Congratulations, {name}')



def main():
    name = welcome_user()
    brain_gcd(name)


if __name__ == '__main__':
    main()