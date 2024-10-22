import random

def is_prime(num):
    """Проверяет, является ли число простым."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_question_answer():
    """Генерирует вопрос и правильный ответ."""
    number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    return number, correct_answer
