def quiz_game():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
            "answer": "A"
        },
        {
            "question": "Which language are we learning?",
            "options": ["A. Java", "B. Python", "C. C++", "D. PHP"],
            "answer": "B"
        },
        {
            "question": "What is 5 + 5?",
            "options": ["A. 8", "B. 9", "C. 10", "D. 11"],
            "answer": "C"
        }
    ]

    score = 1

    for item in questions:
        print("\n" + item["question"])

        for option in item["options"]:
            print(option)

        user_answer = input("Enter your answer: ").upper()

        if user_answer == item["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer!")

    print(f"\nYour final score is {score}/{len(questions)}")


if __name__ == "__main__":
    quiz_game()