# игра "Прогрессия"
from random import randint


GAME_CONDITION = 'What number is missing in the progression?'


def progression_generation():
    random_len = randint(1, 100)
    random_step = randint(1, 10)
    lst = [str(i) for i in range(1, 100, random_step)][:random_len]
    return lst


def get_game():
    lst = progression_generation()
    random_integer = randint(0, len(lst) - 1)
    result = (lst[random_integer])
    lst[random_integer] = '..'
    question = ('Question: ' + (' '.join(lst)))
    return result, question
