from random import randint

TASK = 'What number is missing in the progression?'


def get_round():
    start = randint(1, 100)
    step = randint(1, 10)
    sequence = progression(start, step)
    num_random = randint(0, 9)
    true_answer = sequence[num_random]
    sequence[num_random] = '..'
    sequence = ' '.join(sequence)
    return sequence, true_answer


def progression(start, step):
    end = start + 10 * step
    return list(map(str, range(start, end, step)))
