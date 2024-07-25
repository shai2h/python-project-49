from brain_games.scripts.run_games import run_game
from brain_games.games.brain_prime import generate_prime_question
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(generate_prime_question, rules, name)


if __name__ == '__main__':
    main()
