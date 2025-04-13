import random

# Function to get a valid guess from the user
def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input! Please enter a number.")

# Main game function
def guess_the_number():
    # The number to guess (randomly chosen between 1 and 100)
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Maximum number of attempts allowed

    print("Welcome to Guess the Number!")
    print("I have chosen a number between 1 and 100. Can you guess it?")
    print(f"You have {max_attempts} attempts to guess the correct number.")

    # Game loop
    while attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1

        if guess < number_to_guess:
            print(f"Too low! You have {max_attempts - attempts} attempts remaining.")
        elif guess > number_to_guess:
            print(f"Too high! You have {max_attempts - attempts} attempts remaining.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly in {attempts} attempts.")
            break
    else:
        print(f"Sorry! You've used all your attempts. The correct number was {number_to_guess}.")

# Main program to run the game
if __name__ == "__main__":
    guess_the_number()
