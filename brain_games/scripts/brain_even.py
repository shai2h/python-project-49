from brain_games.cli import welcome_user
import random
from welcome_user import name

def main():
    welcome_user()


def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    while True:
        random_num = random.randint(1, 20)
        print(f'Question: {random_num}')
        answer = input("Your answer: ")
        if answer % 2 == 0:
            print('Correct!')
        else:
            print(f"Let's try again, {name}")
            break
    
    
    


brain_even()

if __name__ == '__main__':
    brain_even()
