# движок для игр ака общая логика
from brain_games.cli import welcome
import prompt


def start_game(game):
    name = welcome()
    print(game.GAME_CONDITION)
    counter = 0
    while counter != 3:
        result, question = game.get_game()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer != result:
            print(f"'{answer}' is wrong answer ;(., "
                  f"Correct answer was '{result}'.\
                    \nLet's try again, {name}!")
            return
        else:
            print('Correct!')
            counter += 1
    print(f'Congratulations, {name}!')
