from random import randint

TASK = 'Answer "yes" if number even otherwise answer "no"'


def get_round():
    number = randint(0, 100)
    return number, 'no' if is_odd(number) else 'yes'


def is_odd(number):
    return number % 2
