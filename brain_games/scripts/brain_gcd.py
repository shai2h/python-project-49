from brain_games.scripts.run_games import run_game
from brain_games.games.brain_gcd import generate_gcd_question
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    rules = 'Find the greatest common divisor of given numbers.'
    run_game(generate_gcd_question, rules, name)


if __name__ == '__main__':
    main()
