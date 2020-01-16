from random import randint

TASK = 'Find the greatest common divisor of given numbers'


def get_round():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    true_answer = str(gcd(number1, number2))
    return f'{number1} {number2}', true_answer


def gcd(a, b):
    return gcd(b, a % b) if b else a
