# Игра "Калькулятор"
from random import randint, choice


ARITHMETIC_OPERATORS = ['+', '-', '*']
GAME_RULE = "What is the result of the expression?"
MAX_INTEGER = 10
MIN_INTEGER = 1


def calculate_expression(operator: str, num1: int, num2: int) -> str:

    correct_answer: int = 0
    if operator == '+':
        correct_answer = num1 + num2
    if operator == '-':
        correct_answer = num1 - num2
    if operator == '*':
        correct_answer = num1 * num2
    return str(correct_answer)


def game_utils() -> tuple:
    first_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    second_number: int = randint(MIN_INTEGER, MAX_INTEGER)
    operator: str = choice(ARITHMETIC_OPERATORS)
    question: str = f'Question: {first_number} {operator} ' \
                    f'{second_number}'
    correct_answer: str = calculate_expression(operator,
                                               first_number,
                                               second_number)
    return question, correct_answer
