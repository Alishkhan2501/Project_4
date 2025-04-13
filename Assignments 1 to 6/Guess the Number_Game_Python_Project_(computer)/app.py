import random

# Function to get feedback from the user about the computer's guess
def get_feedback():
    while True:
        feedback = input("Is my guess too high (h), too low (l), or correct (c)? ").strip().lower()
        if feedback in ['h', 'l', 'c']:
            return feedback
        else:
            print("Invalid input! Please enter 'h' for too high, 'l' for too low, or 'c' for correct.")

# function where the computer guesses the number
def computer_guesses_number():
    print("\n🎮 Welcome to 'Guess the Number (Computer Edition)'!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")

    low = 1
    high = 100
    attempts = 0

    while True:
        attempts += 1
        guess = random.randint(low, high)
        print(f"\nAttempt {attempts}: My guess is {guess}.")
        
        feedback = get_feedback()

        if feedback == 'c':
            print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts.")
            break
        elif feedback == 'h':
            high = guess - 1  
        elif feedback == 'l':
            low = guess + 1  

        # Check for invalid range (this ensures the game logic doesn't break)
        if low > high:
            print("Something went wrong! Please check your feedback inputs.")
            break

# Main program to run the game
if __name__ == "__main__":
    computer_guesses_number()

