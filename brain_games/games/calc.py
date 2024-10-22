import random
import operator

DESCRIPTION = "What is the result of the expression?"

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

def generate_question_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(list(OPERATIONS.keys()))

    question = f"{number1} {operation} {number2}"
    correct_answer = str(OPERATIONS[operation](number1, number2))

    return question, correct_answer

def run_game():
    print(DESCRIPTION)
    rounds = 3
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(rounds):
        question, correct_answer = generate_question_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")



