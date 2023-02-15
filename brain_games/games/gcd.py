# игра "НОД"
from random import randint
from math import gcd


GAME_CONDITION = 'Find the greatest common divisor of given numbers.'


def get_game():
    random_num_1 = randint(0, 100)
    random_num_2 = randint(0, 100)
    question = str(f'Question: {random_num_1} {random_num_2}')
    result = gcd(random_num_1, random_num_2)
    return str(result), question
