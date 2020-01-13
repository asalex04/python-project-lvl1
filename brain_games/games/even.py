from random import randint

TASK = 'Answer "yes" if number even otherwise answer "no"'


def get_game():
    number = randint(0, 100)
    return number, 'no' if is_even(number) else 'yes'


def is_even(number):
    return number % 2
