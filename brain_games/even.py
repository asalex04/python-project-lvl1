import prompt
from random import randint


def main():
    print('\nWelcome to the Brain Games!\n'
          'Answer "yes" if number even otherwise answer "no".\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    start(name)


def start(name):
    for i in range(3):
        number = randint(0, 100)
        print(f'Question: {number}')
        answer = prompt.string('You answer: ')
        if answer in ('yes', 'no'):
            if number % 2:
                if answer == 'yes':
                    print(f"'yes' is wrong answer;(. Correct answer was 'no'. "
                          f"Let's try again, {name}!\n")
                    break
                print('Correct')
                continue
            else:
                if answer == 'no':
                    print(f"'no' is wrong answer;(. Correct answer was 'Yes'. "
                          f"Let's try again, {name}!\n")
                    break
                print('Correct')
                continue
        print(f"{answer} is wrong answer; Let's try again, {name}!\n")
        break


if __name__ == '__main__':
    main()
