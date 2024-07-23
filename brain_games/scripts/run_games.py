from brain_games.utils import is_game_complete

def run_game(question_func, rules, name):
    target_score = 0
    target_score_needed = 3
    print(rules)
    while is_game_complete(target_score, target_score_needed):
        question, correct_answer = question_func()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        try:
            if str(user_answer).strip() == str(correct_answer).strip():
                target_score += 1
                print('Correct!')
            else:
                print(
                    f"'{user_answer}' is wrong answer ;(.\n"
                    f"Correct answer was '{correct_answer}'."
                )
                print(f"Let's try again, {name}!")
                break
        except ValueError:
            print(
                f"'{user_answer}' is wrong answer ;(.\n"
                f"Correct answer was '{correct_answer}'."
            )
            break
    if target_score == target_score_needed:
        print(f'Congratulations, {name}!')