import random

def choose_word():
    # Function to choose a random word from a predefined list
    words = ["hangman", "python", "programming", "challenge", "developer", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    # Function to display the word with guessed letters filled in
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "  # Append the letter if guessed
        else:
            display += "_ "  # Append underscore if not guessed
    return display.strip()

def hangman():
    max_attempts = 6  # Maximum number of incorrect attempts allowed
    incorrect_attempts = 0  # Counter for incorrect attempts
    guessed_letters = []  # List to store guessed letters
    word_to_guess = choose_word()  # Select a word to guess

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))  # Display the initial state of the word

    while incorrect_attempts < max_attempts:
        guess = input("Guess a letter: ").lower()  # Prompt user for a letter guess and convert to lowercase

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        # Check if letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)  # Add guessed letter to the list

        # Check if guessed letter is not in the word
        if guess not in word_to_guess:
            incorrect_attempts += 1  # Increment incorrect attempts counter
            print(f"Incorrect guess! {max_attempts - incorrect_attempts} attempts remaining.")
        else:
            print("Good guess!")

        current_display = display_word(word_to_guess, guessed_letters)  # Update display of the word
        print(current_display)  # Print the current display

        # Check if all letters in the word have been guessed
        if "_" not in current_display:
            print("Congratulations! You guessed the word!")
            break

    # If loop completes without guessing the word
    if "_" in current_display:
        print(f"Sorry, you've run out of attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
