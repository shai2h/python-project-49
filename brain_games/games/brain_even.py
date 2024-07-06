from brain_games.cli import welcome_user
from brain_games.utils import get_random_number, get_user_answer, is_game_complete


def brain_even(name):

    print('Answer "yes" if the number is even, otherwise answer "no".')

    target_score = 0
    target_score_needed = 3

    yes_answer  = 'yes'
    no_answer = 'no'

    while is_game_complete(target_score, target_score_needed):
        random_num = get_random_number(0, 20)
        
        print(f'Question: {random_num}')  
        user_answer = get_user_answer()
        if (user_answer != yes_answer) and (user_answer != no_answer):
            print(f"Let's try again, {name}!")
            break

        
        if (random_num % 2 == 0 and user_answer.lower() == yes_answer) or (random_num % 2 != 0 and user_answer.lower() == no_answer):
            print('Correct!')
            target_score += 1

        elif (random_num %2 != 0 and user_answer.lower() == yes_answer) or (random_num % 2 == 0 and user_answer.lower() == no_answer):
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
    
    if target_score == target_score_needed:
        print(f'Congratulations, {name}')

    

def main():
    name = welcome_user()
    brain_even(name)


if __name__ == '__main__':
    main()
