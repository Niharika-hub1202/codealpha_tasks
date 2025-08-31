import random

def hangman():
    words = ["python", "programming", "internship", "codealpha", "project"]
    chosen_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(chosen_word))

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        # Display current progress
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in chosen_word])
        print(" ".join(display_word))

        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word:", chosen_word)
            break
    else:
        print("😢 Out of attempts! The word was:", chosen_word)

if __name__ == "__main__":
    hangman()
