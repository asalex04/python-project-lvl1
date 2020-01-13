from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def get_game():
    number = randint(0, 200)
    return number, is_simple1(number)


def is_simple1(num):
    return 'no' if [i for i in range(2, num) if num % i == 0] else 'yes'
