import re
import prompt
from random import randint, choice


def main():
    print('\nWelcome to the Brain Games!\n'
          'Answer "yes" if given number is prime. Otherwise answer "no".\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    run(name)


def run(name):
    for i in range(3):
        number = randint(0, 200)
        print(f'Question: {number}')
        answer = prompt.string('You answer: ')
        if answer != is_simple1(number):
            print(f'{answer} is wrong answer ;(. Correct answer'
                  f' was {is_simple1(number)}.\n' f'Let\'s try again, {name}!\n')
            break
        else:
            print(f'Correct!')


def is_simple1(num):
    return 'no' if [i for i in range(2, num) if num % i == 0] else 'yes'


if __name__ == '__main__':
    main()
