import random
from brain_games.games.brain_progression import generate_progression, hide_element


def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    length = random.randint(5, 10)
    progression = generate_progression(length)
    progression_with_hidden, hidden_value = hide_element(progression)

    print("What number is missing in the progression?")
    print("Question:", ' '.join(map(str, progression_with_hidden)))

    user_answer = input("Your answer: ")

    if int(user_answer) == hidden_value:
        print("Correct!")
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{hidden_value}'.")
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    play_game()
