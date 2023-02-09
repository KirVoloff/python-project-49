#!/usr/bin/env python3
from brain_games.cli import welcome
from brain_games.mygame import game_progression


def main():
    name = welcome()
    round = 0
    print('What number is missing in the progression?')
    while round != 3:
        answer, element = game_progression()
        if answer == element:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong ;(. Correct answer was '{element}'")
            print(f"Let's try again, {name}!")
            break
        round += 1
        if round == 3:
            print(f"Congratulations, {name}! ")


if __name__ == '__main__':
    main()
