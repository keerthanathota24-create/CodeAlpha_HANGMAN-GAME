import random
# List of words
words = ["apple", "tiger", "chair", "house", "green"]
# Select random word
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6
print(" Hangman Game ")
while wrong_guesses < max_wrong:
    display_word = ""
    # Show guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:", display_word)
    # Check win
    if "_" not in display_word:
        print("You guessed the word correctly!")
        break
    guess = input("Enter a letter: ")
    # Avoid duplicate guesses
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    guessed_letters.append(guess)
    # Check correct or wrong
    if guess in word:
        print("Correct Guess!")
    else:
        wrong_guesses += 1
        print("Wrong Guess!")
        print("Remaining chances:", max_wrong - wrong_guesses)
# If user loses
if wrong_guesses == max_wrong:
    print("\nYou lost!")
    print("The word was:", word)