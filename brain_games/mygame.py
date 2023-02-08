import random


def game_even():
    winner = ''
    round = 0
    while round != 3:
        number = random.randint(0, 1000)
        print(f"Question: {number}")
        answer = (input('Your answer: '))
        if number % 2 == 0 and answer == "yes":
            print("Correct!")
        elif number % 2 != 0 and answer == "no":
            print("Correct!")
        else:
            break
        round += 1
        if round == 3:
            return winner


def game_progression():
    start = random.randint(0, 40)
    end = random.randint(50, 100)
    step = random.randint(2, 6)
    progression = list(range(start, end, step))
    Question = progression[:10]      # ограничение прогрессии
    element = random.choice(Question)      # рандомный элемент
    if element in Question:
        for index, value in enumerate(Question):
            if value == element:
                Question[index] = '..'      # процесс замены цифры на ..
    for_print = " ".join(map(str, Question))
    print(f"Question: {for_print}")
    answer = int(input('Your answer: '))
    return answer, element


