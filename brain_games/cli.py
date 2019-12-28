import prompt
from brain_games import even


def run():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    even.main()
