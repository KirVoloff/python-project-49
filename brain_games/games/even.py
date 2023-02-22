# игра "Чётность/нечётность"
from random import randint


GAME_MESSAGE = "Answer 'yes' if the number is even otherwise answer 'no'!"
MIN_INTEGER = 1
MAX_INTEGER = 100


def is_even(number: int) -> bool:
    return number % 2 == 0


def game_utils() -> tuple:
    random_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    question: str = f"Question: {random_number}"
    if is_even(random_number):
        correct_answer: str = 'yes'
    else:
        correct_answer: str = 'no'
    return question, correct_answer
