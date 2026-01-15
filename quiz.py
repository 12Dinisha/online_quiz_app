def run_quiz():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
            "answer": "B"
        },
        {
            "question": "Which language is used for Data Science?",
            "options": ["A. HTML", "B. CSS", "C. Python", "D. XML"],
            "answer": "C"
        },
        {
            "question": "What does API stand for?",
            "options": [
                "A. Application Programming Interface",
                "B. Advanced Program Interaction",
                "C. Applied Programming Internet",
                "D. Application Process Integration"
            ],
            "answer": "A"
        }
    ]

    score = 0

    print("\nOnline Quiz Platform")
    print("---------------------")

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("\nQuiz Completed!")
    print(f"Your Score: {score}/{len(questions)}")


def main():
    print("Welcome to the Quiz!")
    start = input("Press Y to start the quiz: ").upper()

    if start == "Y":
        run_quiz()
    else:
        print("Quiz exited.")


if __name__ == "__main__":
    main()
