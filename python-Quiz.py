# =====================================
# Project Name: Quiz Application
# Author: Tejas Sadafule
# Language: Python
# Description: A simple command-line quiz application
# Version: 1.0
# =====================================

# List of questions
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Processing Unit", "C. Central Program Unit", "D. Control Processing Unit"],
        "answer": "A"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /*", "C. #", "D. --"],
        "answer": "C"
    }
]

# Initialize score
score = 0

print("===== Welcome to the Quiz Application ===== - python-Quiz.py:41")

# Loop through all questions
for q in questions:

    print("\n - python-Quiz.py:46" + q["question"])

    # Display options
    for option in q["options"]:
        print(option)

    # Get user's answer
    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    # Check answer
    if user_answer == q["answer"]:
        print("Correct Answer! - python-Quiz.py:57")
        score += 1
    else:
        print("Wrong Answer! - python-Quiz.py:60")
        print("Correct answer is: - python-Quiz.py:61", q["answer"])

# Display final score
print("\n===== Quiz Completed ===== - python-Quiz.py:64")
print("Your Score: - python-Quiz.py:65", score, "/", len(questions))

percentage = (score / len(questions)) * 100

print("Percentage: - python-Quiz.py:69", percentage, "%")