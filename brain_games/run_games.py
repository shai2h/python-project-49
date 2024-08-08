import prompt  # type: ignore``


def run_game(game_module):
    name = welcome_user()
    rules = game_module.RULES
    question_func = game_module.get_question_and_answer

    target_score = 0
    target_score_needed = 3

    print(rules)
    while target_score < target_score_needed:
        question, correct_answer = question_func()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == correct_answer:
            target_score += 1
            print('Correct!')
        else:
            print(
                f"'{user_answer}' is wrong answer ;(.\n"
                f"Correct answer was '{correct_answer}'."
            )
            break
    print(f"Let's try again, {name}!")
    if target_score == target_score_needed:
        print(f'Congratulations, {name}!')


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")
    return name
