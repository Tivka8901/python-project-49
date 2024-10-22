from brain_games.games.brain_prime import get_question_answer

def play_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):  # Три вопроса
        number, correct_answer = get_question_answer()
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return  # Завершить игру при неверном ответе

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    play_game()
