# Import the data from our database file
from quiz_database import question_bank, options

print("********************************")
print("Welcome to My Quiz Game")
print("********************************")


def check_answer(user_guess, correct_answer):
    """
    Checks if the user's guess matches the correct answer.
    Returns True if correct, False otherwise.
    """
    if user_guess == correct_answer:
        return True
    else:
        return False


score = 0

# Loop through every question in the question_bank
for question_num in range(len(question_bank)):
    print("\n--------------------------------")

    # 1. Print the Question
    # question_bank[question_num] gives the dictionary
    # ["text"] gives the question string
    print(question_bank[question_num]["text"])

    # 2. Print the Options for this specific question
    for i in options[question_num]:
        print(i)

    # 3. Take User Input
    guess = input("Enter your answer (A/B/C/D): ").upper()

    # 4. Check if answer is correct
    correct_ans = question_bank[question_num]["answer"]
    is_correct = check_answer(guess, correct_ans)

    if is_correct:
        print("Correct Answer!")
        score += 1
    else:
        print("Incorrect Answer!")
        print(f"The correct answer is: {correct_ans}")

    # 5. Display current score
    # question_num + 1 is used because index starts at 0
    print(f"Your current score is {score}/{question_num + 1}")

print("\n--------------------------------")
print("       GAME OVER       ")
print("--------------------------------")

# Final Results
print(f"You have given {score} correct answers.")
# Calculate percentage: (score / total_questions) * 100
percentage = (score / len(question_bank)) * 100
print(f"Your Score is {percentage}%")