from brain_games.cli import welcome_user
from brain_games.games.brain_progression import brain_progression


def main():
    name = welcome_user()
    brain_progression(name)


if __name__ == '__main__':
    main()
