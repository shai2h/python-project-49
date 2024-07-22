from brain_games.cli import welcome_user
from brain_games.games.brain_prime import brain_prime


def main():
    name = welcome_user()
    brain_prime(name)


if __name__ == '__main__':
    main()
