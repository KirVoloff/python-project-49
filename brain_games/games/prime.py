# игра "Простое ли число?"
from random import randint


GAME_MESSAGE: str = ''' Answer \"yes\" if given number is prime. 
Otherwise answer \"no\".'''
MIN_INTEGER = 1
MAX_INTEGER = 100


def is_prime(number: int) -> bool:
    if number <= 1:  # Negative numbers can't be prime
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def game_utils() -> tuple:
    random_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    question: str = f"Question: {random_number}"
    if is_prime(random_number):
        correct_answer: str = 'yes'
    else:
        correct_answer: str = 'no'
    return question, correct_answer
