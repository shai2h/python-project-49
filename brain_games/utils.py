def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
