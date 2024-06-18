import prompt  # type: ignore


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}")


# Две пустые строки
# Пустая строка в конце файла
