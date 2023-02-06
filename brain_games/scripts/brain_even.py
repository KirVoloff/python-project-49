#!/usr/bin/env python3

def main():
    if __name__ == '__main__':
        main()


def game1():

    from brain_games.cli import welcome

    name = welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    from brain_games.mygame import game_even

    if game_even() == '':
        print(f"Congratulations, {name}! ")
    else:
        print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")

game1()
