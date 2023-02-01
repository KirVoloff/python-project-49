import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print('Hello,' + name + "!")
welcome_user()

def question1():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    number1 = random.randint(1, 1000)
    print('Question: ' + str(number1))
    answer1 = prompt.string('Your answer: ')
    if number1%2==0 and answer1 == 'yes':
     print('Correct!')
    if number1%2!=0 and answer1 == 'yes':
     print(f''''yes' is wrong answer ;\(. Correct answer was 'no'. 
Let's try again, {name} '!''')
     exit()
    if number1%2!=0 and answer1 == 'no':
     print('Correct!')
    if number1%2==0 and answer1 == 'no':
     print(f''''no' is wrong answer ;\(. Correct answer was 'yes'. 
Let's try again, {name} '!''')
     exit()
    if answer1 != 'yes' or 'no':
     exit()
question1()

def question2():
    number2 = random.randint(1, 1000)
    print('Question: ' + str(number2))
    answer2 = prompt.string('Your answer: ')
    if number2%2==0 and answer2 == 'yes':
     print('Correct!')
    if number2%2!=0 and answer2 == 'yes':
     print(f''''yes' is wrong answer ;\(. Correct answer was 'no'. 
Let's try again, {name} '!''')
     exit()
    if number2%2!=0 and answer2 == 'no':
     print('Correct!')
    if number2%2==0 and answer2 == 'no':
     print(f''''no' is wrong answer ;\(. Correct answer was 'yes'. 
Let's try again, {name} '!''')
     exit() 
    if answer2 != 'yes' or 'no':
     exit()
question2()


def question3():
    number3 = random.randint(1, 1000)
    print('Question: ' + str(number3))
    answer3 = prompt.string('Your answer: ')
    if number3%2==0 and answer3 == 'yes':
     print('Correct!')
    if number3%2!=0 and answer3 == 'yes':
     print(f''''yes' is wrong answer ;\(. Correct answer was 'no'. 
Let's try again, {name} '!''')
     exit()
    if number3%2!=0 and answer3 == 'no':
     print('Correct!')
    if number3%2==0 and answer3 == 'no':
     print(f''''no' is wrong answer ;\(. Correct answer was 'yes'. 
Let's try again, {name} '!''')
     exit()
    if answer3 != 'yes' or 'no':
     exit()
question3()

print("Congratulations," + name + "!")
