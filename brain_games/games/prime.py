from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def get_round():
    number = randint(0, 100)
    return number, is_prime(number)


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return 'no'
    return 'yes'
