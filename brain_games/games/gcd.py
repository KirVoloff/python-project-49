# игра "НОД"
from random import randint
from math import gcd


GAME_RULE = "Find the greatest common divisor of given numbers."
MIN_INTEGER = 1
MAX_INTEGER = 10


def game_utils() -> tuple:
    first_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    second_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    largest_divisor: int = gcd(first_number, second_number)
    question: str = f"Question: {first_number} {second_number}"
    return question, str(largest_divisor)
