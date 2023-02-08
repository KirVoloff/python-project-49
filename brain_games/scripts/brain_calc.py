#!/usr/bin/env python3
from brain_games.cli import welcome
import random


def main():
    name = welcome()
    round = 0
    print('What is the result of the expression?')
    while round != 3:
        number_1 = random.randint(0, 100)
        number_2 = random.randint(0, 100)
        math_operation = random.choice(['+', '*', '-'])
        Question = str(number_1) + ' ' + math_operation + ' ' + str(number_2)

        def variation_1():
            variation = {
                math_operation == "+": number_1 + number_2,
                math_operation == "-": number_1 - number_2,
                math_operation == "*": number_1 * number_2
            }
            return variation[True]
        print(f"Question: {Question}")
        answer = int(input('Your answer: '))
        if answer == variation_1():
            print("Correct")
        else:
            print(f"'{answer}' is wrong ;(. Correct answer was '{variation_1()}'")
            print(f"Let's try again, {name}!")
            break
        round += 1
        if round == 3:
            print(f"Congratulations, {name}! ")


if __name__ == '__main__':
    main()
