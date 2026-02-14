import random

WORDS = [
    "python",
    "variable",
    "function",
    "computer",
    "terminal",
    "internet",
    "project",
    "practice",
    "algorithm",
    "developer",
]


def masked_word(word, guessed):
    return " ".join([ch if ch in guessed else "_" for ch in word])


def play_round():
    word = random.choice(WORDS)
    guessed_letters = set()
    wrong_letters = set()
    attempts_left = 7

    print("Guess the word")

    while attempts_left > 0:
        print()
        print(masked_word(word, guessed_letters))
        print(f"Wrong letters: {' '.join(sorted(wrong_letters)) if wrong_letters else 'none'}")
        print(f"Attempts left: {attempts_left}")

        guess = input("Guess a letter or full word: ").strip().lower()
        if not guess.isalpha():
            print("Use letters only")
            continue

        if len(guess) > 1:
            if guess == word:
                print(f"Correct. The word was {word}")
                return True
            attempts_left -= 1
            print("Wrong word guess")
            continue

        letter = guess
        if letter in guessed_letters or letter in wrong_letters:
            print("Already guessed")
            continue

        if letter in word:
            guessed_letters.add(letter)
            if all(ch in guessed_letters for ch in word):
                print(masked_word(word, guessed_letters))
                print(f"You won. The word was {word}")
                return True
        else:
            wrong_letters.add(letter)
            attempts_left -= 1
            print("Wrong letter")

    print(f"You lost. The word was {word}")
    return False


def main():
    wins = 0
    losses = 0

    while True:
        result = play_round()
        if result:
            wins += 1
        else:
            losses += 1

        print(f"Score -> Wins: {wins}, Losses: {losses}")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            break


if __name__ == "__main__":
    main()
