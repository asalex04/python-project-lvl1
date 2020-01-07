import prompt
from random import randint


def main():
    print('\nWelcome to the Brain Games!\n'
          'Find the greatest common divisor of given numbers.\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    run(name)


def run(name):
    for i in range(3):
        number1 = randint(0, 100)
        number2 = randint(0, 100)
        true_answer = gcd(number1, number2)
        print(f'Question: {number1} {number2}')
        answer = prompt.string('You answer: ')
        if answer != true_answer:
            print(f'{answer} is wrong answer ;(. Correct answer'
                  f' was {true_answer}.\n' f'Let\'s try again, {name}!\n')
            break
        else:
            print(f'Correct!')


def gcd(a, b):
    return str(gcd(b, a % b) if b else a)


if __name__ == '__main__':
    main()
