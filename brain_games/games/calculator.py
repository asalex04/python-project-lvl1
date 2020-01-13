from random import randint, choice


TASK = 'What is the result of the expression?'


def true_answer(num1, num2, math):
    return count(num1, num2, math)


def get_game():
    number1 = randint(0, 100)
    number2 = randint(0, 100)
    math = choice(['+', '-', '*', '/'])
    return (
        f'{number1} {math} {number2}',
        f'{true_answer(number1, number2, math)}'
    )


def count(x, y, sign):
    if sign == '+':
        res = x + y
    elif sign == '-':
        res = x - y
    elif sign == '*':
        res = x * y
    else:
        res = x / y if y != 0 else print('Деление на ноль')
        return f'{res:.2f}'
    return f'{res}'
