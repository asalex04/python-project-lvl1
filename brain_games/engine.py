from brain_games.cli import get_user_answer, get_user_name

ROUNDS = 3


def description(task):
    print(f'{task}\n')


def run(game=None):
    print('Welcome to the Brain Games!\n')
    if game:
        description(game.TASK)
    name = get_user_name()
    if not game:
        return
    for _ in range(ROUNDS):
        question, true_answer = game.get_game()
        print(f'Question: {question}')
        answer = get_user_answer()
        if answer != true_answer:
            print(f'{answer} is wrong answer ;(. Correct answer'
                  f' was {true_answer}.\n' f'Let\'s try again, {name}!\n')
            return
        print(f'Correct!\n')
    print(f'Congratulations, {name}!\n')
