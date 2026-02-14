import json
import random
from pathlib import Path

SCORE_FILE = Path("quiz_master_scores.json")

QUESTIONS = [
    {
        "question": "Which keyword defines a function in Python?",
        "choices": ["1) func", "2) def", "3) function", "4) lambda"],
        "answer": "2",
    },
    {
        "question": "What is the output type of input()?",
        "choices": ["1) int", "2) float", "3) str", "4) bool"],
        "answer": "3",
    },
    {
        "question": "Which data type is mutable?",
        "choices": ["1) tuple", "2) string", "3) list", "4) int"],
        "answer": "3",
    },
    {
        "question": "What does len([1,2,3,4]) return?",
        "choices": ["1) 3", "2) 4", "3) 5", "4) Error"],
        "answer": "2",
    },
    {
        "question": "Which loop is best when count is known?",
        "choices": ["1) for", "2) while", "3) if", "4) try"],
        "answer": "1",
    },
    {
        "question": "What is 3 ** 2 in Python?",
        "choices": ["1) 6", "2) 8", "3) 9", "4) 32"],
        "answer": "3",
    },
    {
        "question": "Which statement handles exceptions?",
        "choices": ["1) if", "2) except", "3) for", "4) with"],
        "answer": "2",
    },
    {
        "question": "Which method adds one item to list end?",
        "choices": ["1) add", "2) push", "3) append", "4) insert_end"],
        "answer": "3",
    },
]


def load_best_score():
    if SCORE_FILE.exists():
        try:
            data = json.loads(SCORE_FILE.read_text(encoding="utf-8"))
            return int(data.get("best_score", 0))
        except (json.JSONDecodeError, ValueError):
            return 0
    return 0


def save_best_score(score):
    SCORE_FILE.write_text(json.dumps({"best_score": score}, indent=2), encoding="utf-8")


def ask_question(item, index):
    print(f"\nQuestion {index}")
    print(item["question"])
    for choice in item["choices"]:
        print(choice)
    answer = input("Your answer (1-4): ").strip()
    is_correct = answer == item["answer"]
    if is_correct:
        print("Correct")
    else:
        correct_text = item["choices"][int(item["answer"]) - 1]
        print(f"Wrong. Correct answer: {correct_text}")
    return is_correct


def run_quiz():
    best_score = load_best_score()
    print(f"Best score so far: {best_score}/{len(QUESTIONS)}")

    try:
        count = int(input(f"How many questions (1-{len(QUESTIONS)}): ").strip())
    except ValueError:
        count = len(QUESTIONS)

    if count < 1:
        count = 1
    if count > len(QUESTIONS):
        count = len(QUESTIONS)

    selected = random.sample(QUESTIONS, count)
    score = 0
    missed = []

    for i, question in enumerate(selected, start=1):
        if ask_question(question, i):
            score += 1
        else:
            missed.append(question["question"])

    print("\nQuiz complete")
    print(f"Score: {score}/{count}")
    percent = (score / count) * 100
    print(f"Percent: {percent:.1f}%")

    if missed:
        print("Questions to review:")
        for line in missed:
            print(f"- {line}")

    if score > best_score:
        save_best_score(score)
        print("New best score saved")


if __name__ == "__main__":
    while True:
        run_quiz()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break
