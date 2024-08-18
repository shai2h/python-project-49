import prompt

# Константа для количества раундов
ROUNDS_COUNT = 3


def run_game(game_module):
    name = welcome_user()

    print(game_module.RULE)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game_module.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(.\n"
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name
