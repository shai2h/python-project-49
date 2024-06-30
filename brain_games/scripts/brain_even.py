from brain_games.cli import welcome_user
import random

def brain_even(name):


    print('Answer "yes" if the number is even, otherwise answer "no".')

    user_correct_answers = 0
    user_correct_answers_needed = 3

    while user_correct_answers < user_correct_answers_needed:
        random_num = random.randint(1, 20)
        print(f'Question: {random_num}')  
        user_answer = str(input('Your answer: '))

        if (random_num % 2 == 0 and user_answer.lower() == 'yes') or (random_num % 2 != 0 and user_answer.lower() == 'no'):
            print('Correct!')
            user_correct_answers += 1
        elif (random_num % 2 != 0 and user_answer.lower() == 'yes'):
            print("'no' is wrong answer ;(. Correct answer was 'yes'.")
            print(f"Let's try again, {name}!")
            break
        elif (random_num % 2 == 0 and user_answer.lower() == 'no'):
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print(f"Let's try again, {name}!")
            break

    print(f'Congratulations, {name}')

    

def main():
    name = welcome_user()
    brain_even(name)




if __name__ == '__main__':
    main()
