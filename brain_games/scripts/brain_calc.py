from brain_games.scripts.run_games import run_game
from brain_games.games.brain_calc import generate_calc_question
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    rules = 'What is the result of the expression?'
    run_game(generate_calc_question, rules, name)


if __name__ == '__main__':
    main()
