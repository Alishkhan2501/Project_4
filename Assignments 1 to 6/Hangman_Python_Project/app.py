import random
import string
from words import words  # Assuming you have a list of words in this file

# This function picks a valid word from the list
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:  # Make sure it's not a word with dashes or spaces
        word = random.choice(words)
    return word

# Function to display the current progress of the word
def display_word_progress(word, used_letters):
    return ' '.join([letter if letter in used_letters else '-' for letter in word])

# Function to start a game of Hangman
def hangman():
    print("\nWelcome to Hangman!")
    
    # Ask the player for the difficulty level (number of lives)
    difficulty = input("Choose your difficulty (Easy / Medium / Hard): ").lower()
    if difficulty == 'easy':
        lives = 8
    elif difficulty == 'medium':
        lives = 6
    elif difficulty == 'hard':
        lives = 4
    else:
        print("Invalid choice, defaulting to medium difficulty.")
        lives = 6

    word = get_valid_word(words).upper()  # Get a random valid word and convert to uppercase
    word_letters = set(word)  # Set of unique letters in the word
    alphabet = set(string.ascii_uppercase)  # Set of all uppercase letters
    used_letters = set()  # Set to store used letters
    incorrect_letters = set()  # Set to store incorrect guesses

    print(f"\nThe word has {len(word)} letters.\n")

    while len(word_letters) > 0 and lives > 0:
        print(f'\nYou have {lives} lives left and you have used these letters: {", ".join(sorted(used_letters))}')
        print(f'Incorrect guesses: {", ".join(sorted(incorrect_letters))}\n')

        # Display the current state of the word
        print(f"Current word: {display_word_progress(word, used_letters)}\n")

        # Ask the user to guess a letter
        user_letter = input("Guess a letter: ").upper()

        # Ensure the user input is a valid single letter
        if len(user_letter) != 1 or user_letter not in alphabet:
            print("Invalid input. Please enter a single letter from A-Z.\n")
            continue

        # Check if the user already guessed this letter
        if user_letter in used_letters or user_letter in incorrect_letters:
            print(f"You already guessed '{user_letter}'. Try again.\n")
            continue

        # Add the guessed letter to the set of used letters
        if user_letter in word_letters:
            used_letters.add(user_letter)
            word_letters.remove(user_letter)  # Remove the guessed letter from the set
            print(f"Good guess! '{user_letter}' is in the word.\n")
        else:
            incorrect_letters.add(user_letter)
            lives -= 1  # Deduct a life if the guess is wrong
            print(f"Oops! '{user_letter}' is not in the word.\n")

    # Final check: did the player win or lose?
    if lives == 0:
        print(f"\nYou died, sorry. The word was '{word}'. Better luck next time!\n")
    else:
        print(f"\nCongratulations! You guessed the word '{word}' correctly!\n")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (Yes/No): ").lower()
    if play_again == 'yes':
        hangman()  # Start a new game
    else:
        print("Thanks for playing! Goodbye.")

# Start the game
hangman()