# движок для игр ака общая логика
from brain_games.cli import welcome
import prompt


def start_game(game) -> None:
    name: str = welcome()
    print(game.GAME_CONDITION)
    counter = 0
    while counter != 3:
        result, question = game.get_game()
        print(question)
        answer: str = prompt.string("Your answer: ")
        counter += 1
        if answer == result:
            print("Correct!")
        else:
            print(f"{answer} is wrong answer ;(. Correct "
                  f"answer is {correct_answer}")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
