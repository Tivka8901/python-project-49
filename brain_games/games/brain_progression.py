import random

def generate_progression(length=10):
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    progression = [start + step * i for i in range(length)]
    return progression

def hide_element(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'
    return progression, hidden_value
