# игра "Простое ли число?"
from random import randint


GAME_CONDITION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    counter = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            counter += 1
    if counter <= 0:
        return True
    else:
        return False


def get_game():
    random_num = randint(0, 100)
    question = str(f'Question: {random_num}')
    if is_prime(random_num):
        result = 'yes'
    else:
        result = 'no'
    return result, question
