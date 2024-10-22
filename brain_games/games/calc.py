import random
import operator

DESCRIPTION = "What is the result of the expression?"

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

def generate_question_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(list(OPERATIONS.keys()))

    question = f"{number1} {operation} {number2}"
    correct_answer = str(OPERATIONS[operation](number1, number2))

    return question, correct_answer


