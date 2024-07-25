from brain_games.scripts.run_games import run_game
from brain_games.games.brain_progression import generate_progression
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    rules = "What number is missing in the progression?"
    run_game(generate_progression, rules, name)


if __name__ == '__main__':
    main()
