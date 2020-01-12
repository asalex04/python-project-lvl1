import prompt


def get_user_name():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!\n')
    return name


def get_user_answer():
    answer = prompt.string('You answer: ').lower()
    return answer
