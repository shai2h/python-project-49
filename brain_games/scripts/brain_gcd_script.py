from brain_games.cli import welcome_user
from brain_games.games.brain_gcd import brain_gcd


def main():
    name = welcome_user()
    brain_gcd(name)


if __name__ == '__main__':
    main()
