from brain_games.cli import get_user_answer, get_user_name

ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!\n'
          f'{game.TASK}\n')
    name = get_user_name()
    for _ in range(ROUNDS):
        question, true_answer = game.get_round()
        print(f'Question: {question}')
        answer = get_user_answer()
        if answer != true_answer:
            print(f'{answer} is wrong answer ;(. Correct answer'
                  f' was {true_answer}.\n' f'Let\'s try again, {name}!\n')
            return
        print('Correct!\n')
    print(f'Congratulations, {name}!\n')
