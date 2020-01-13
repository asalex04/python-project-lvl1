import re
from random import randint, choice

TASK = 'What number is missing in the progression?'


def get_game():
    start = randint(1, 100)
    step = randint(1, 10)
    sequence = progression(start, step)
    num_random = choice(sequence)
    sequence = ' '.join(sequence)
    new_sequence = re.sub(num_random, '..', sequence)
    return new_sequence, num_random


def progression(start, step):
    end = start + 10 * step
    return list(map(str, [x for x in range(start, end, step)]))
