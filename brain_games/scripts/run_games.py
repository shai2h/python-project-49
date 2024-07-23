from brain_games.utils import is_game_complete


def run_game(question_func, rules, name):
    target_score = 0
    target_score_needed = 3
    print(rules)
    while is_game_complete(target_score, target_score_needed):
        question_result = question_func()
        question, correct_answer = parse_question_result(question_result)
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if check_answer(user_answer, correct_answer):
            target_score += 1
            print('Correct!')
        else:
            print_wrong_answer_message(user_answer, correct_answer, name)
            break
    if target_score == target_score_needed:
        print(f'Congratulations, {name}!')


def parse_question_result(question_result):
    if len(question_result) == 3:
        question1, question2, correct_answer = question_result
        question = f'{question1} {question2}'
    else:
        question, correct_answer = question_result
    return question, correct_answer


def check_answer(user_answer, correct_answer):
    try:
        return str(user_answer).strip() == str(correct_answer).strip()
    except ValueError:
        return False


def print_wrong_answer_message(user_answer, correct_answer, name):
    print(
        f"'{user_answer}' is wrong answer ;(.\n"
        f"Correct answer was '{correct_answer}'."
    )
    print(f"Let's try again, {name}!")
