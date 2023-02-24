# Игра калькулятор
from random import randint, choice


GAME_RULE = 'What is the result of the expression?'
OPERATORS = choice('+-*')


def calculate_expression(num_1, num_2):
    if OPERATORS == '+':
        return num_1 + num_2
    elif OPERATORS == '-':
        return num_1 - num_2
    else:
        return num_1 * num_2


def get_game():
    random_num_1 = randint(1, 99)
    random_num_2 = randint(1, 99)
    question = str(f'Question: {random_num_1} {OPERATORS} {random_num_2}')
    result = calculate_expression(random_num_1, random_num_2)
    return str(result), question
