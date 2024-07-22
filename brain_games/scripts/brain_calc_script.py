from brain_games.cli import welcome_user
from brain_games.games.brain_calc import brain_calc


def main():
    name = welcome_user()
    brain_calc(name)


if __name__ == '__main__':
    main()
