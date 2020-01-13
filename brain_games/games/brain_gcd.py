from random import randint

TASK = 'Find the greatest common divisor of given numbers'


def get_game():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    true_answer = gcd(number1, number2)
    return f'{number1} {number2}', f'{true_answer}'


def gcd(a, b):
    return str(gcd(b, a % b) if b else a)
