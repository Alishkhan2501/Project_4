import random

def get_user_choice():
    """Get and validate the user's input."""
    while True:
        user_input = input("What's your choice? ('r' for Rock, 'p' for Paper, 's' for Scissors): ").lower()
        if user_input in ['r', 'p', 's']:
            return user_input
        print("Invalid input! Please enter 'r', 'p', or 's'.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['r', 'p', 's'])

def choice_to_name(choice):
    """Convert the letter choice to full name."""
    if choice == 'r':
        return "Rock"
    elif choice == 'p':
        return "Paper"
    elif choice == 's':
        return "Scissors"

def is_win(player, opponent):
    """Determine if the player wins."""
    return (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')

def play_round():
    """Play a single round of the game."""
    user = get_user_choice()
    computer = get_computer_choice()

    print(f"\nYou chose: {choice_to_name(user)}")
    print(f"The computer chose: {choice_to_name(computer)}")

    # Check for tie
    if user == computer:
        return "It's a tie!", 0, 0

    # Check if the user wins
    if is_win(user, computer):
        return "You won!", 1, 0

    # If not a tie and user didn't win, user lost
    return "You lost!", 0, 1

def play():
    """Main function to play the game with score tracking."""
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors game!")

    while True:
        result, user_points, computer_points = play_round()

        #  scores
        user_score += user_points
        computer_score += computer_points

        print(f"\n{result}")
        print(f"Your score: {user_score} | Computer's score: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nThanks for playing! Final Score:")
            print(f"Your final score: {user_score}")
            print(f"Computer's final score: {computer_score}")
            break

if __name__ == "__main__":
    play()