import re
import prompt
from random import randint, choice


def main():
    print('\nWelcome to the Brain Games!\n'
          'What number is missing in the progression?\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    run(name)


def run(name):
    for i in range(3):
        start = randint(1, 100)
        step = randint(1, 10)
        sequence = progression(start, step)
        num_random = choice(sequence)
        sequence = ' '.join(sequence)
        new_sequence = re.sub(num_random, '..', sequence)
        print(f'Question: {new_sequence}')
        answer = prompt.string('You answer: ')
        if answer != num_random:
            print(f'{answer} is wrong answer ;(. Correct answer'
                  f' was {num_random}.\n' f'Let\'s try again, {name}!\n')
            break
        else:
            print(f'Correct!')


def progression(start, step):
    end = start + 10 * step
    return list(map(str, [x for x in range(start, end, step)]))


if __name__ == '__main__':
    main()
