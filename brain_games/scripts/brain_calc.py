from brain_games.games.calc import generate_question_answer

DESCRIPTION = "What is the result of the expression?"


def run_game(game_function):
    print(DESCRIPTION)

    for _ in range(3):
        question, correct_answer = game_function()
        print(f"Question: {question}")

        user_answer = input("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
            break
    else:
        print("Congratulations, you answered all questions correctly!")


def main():
    run_game(generate_question_answer)


if __name__ == "__main__":
    main()

