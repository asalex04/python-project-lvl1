import prompt
from random import randint, choice


def main():
    print('\nWelcome to the Brain Games!\n'
          'What is the result of the expression?\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    calculate(name)


def calculate(name):
    for i in range(3):
        number1 = randint(0, 100)
        number2 = randint(0, 100)
        math = choice(['+', '-', '*', '/'])
        true_answer = count(number1, number2, math)
        print(f'Question: {number1} {math} {number2}')
        answer = prompt.string('You answer: ')
        if answer != true_answer:
            print(f'{answer} is wrong answer ;(. Correct answer'
                  f' was {true_answer}.\n' f'Let\'s try again, {name}!\n')
            break
        else:
            print(f'Correct!')


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


if __name__ == '__main__':
    main()
