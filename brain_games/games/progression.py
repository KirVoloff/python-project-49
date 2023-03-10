# игра "Прогрессия"
from random import randint, randrange


GAME_RULE = "What number is missing in the progression?"
NUM_OF_ITERATIONS: int = 10
MIN_START: int = 1
MAX_START: int = 100
MIN_INC: int = 1
MAX_INC: int = 5


def game_utils() -> tuple:
    starting_number: int = randint(MIN_START, MAX_START)
    increment_number: int = randint(MIN_INC, MAX_INC)
    random_index_of_hidden_number: int = randrange(NUM_OF_ITERATIONS)
    progress: str = f'{starting_number} '
    hidden_number: int = 0
    for i in range(NUM_OF_ITERATIONS):
        if random_index_of_hidden_number == i:
            starting_number += increment_number
            hidden_number = starting_number
            progress += '.. '
        else:
            starting_number += increment_number
            progress += f'{starting_number} '
    question: str = f'Question: {progress}'
    return question, str(hidden_number)
