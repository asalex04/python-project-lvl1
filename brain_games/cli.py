import prompt
from brain_games import brain_even


def run():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    brain_even.main()
