import random
import math
from brain_games.engine import play_game

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    correct_answer = str(math.gcd(num1, num2))
    return question, correct_answer

def play_gcd_game():
    play_game(DESCRIPTION, generate_round)
