from brain_games.scripts.run_games import run_game
from brain_games.games.brain_even import generate_even_question
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(generate_even_question, rules, name)


if __name__ == '__main__':
    main()
