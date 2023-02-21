# игра "Чётность/нечётность"
from random import randint


GAME_CONDITION = 'Answer "yes" if the number is even otherwise answer "no".'


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def get_game():
    random_num = randint(1, 100)
    question = str(f'Question: {random_num}')
    if is_even(random_num):
        result = 'yes'
    else:
        result = 'no'
    return result, question
