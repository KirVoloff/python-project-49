# движок запускающий и проверяющий игры
import prompt


def start_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULE)
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
