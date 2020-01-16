from random import randint, choice
from operator import add, sub, mul

TASK = 'What is the result of the expression?'


def get_round():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    math, calculate = choice((('+', add), ('-', sub), ('*', mul)))
    return (
        f'{number1} {math} {number2}',
        str(calculate(number1, number2))
    )
