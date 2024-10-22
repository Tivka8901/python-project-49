import random
import prompt

def is_even(number):
    return number % 2 == 0

def play_even_game():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    rounds_to_win = 3

    while correct_answers < rounds_to_win:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ').lower()

        correct_answer = 'yes' if is_even(number) else 'no'

        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')