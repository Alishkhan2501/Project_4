import random

# Function to prompt for user inputs with validation
def get_input(prompt, valid_input_type=str):
    """Prompt the user for input with validation based on the expected type."""
    while True:
        user_input = input(prompt).strip()
        if valid_input_type == int:
            try:
                return int(user_input)
            except ValueError:
                print("❗ Please enter a valid number.")
        else:
            return user_input

# Function to select a random story template
def get_story_template():
    """Randomly select a story template."""
    templates = [
        """
        Once upon a time, {name} went to a {adjective1} {noun1}. It was a very {adjective2} place, full of strange creatures. 
        {name} decided to {verb} around, exploring the {place}. Suddenly, they found a {noun2} that was {number} times bigger than they expected!
        {name} couldn't believe their eyes and had an amazing adventure.
        """,
        
        """
        On a {adjective1} day, {name} went to {place} to find a {noun1}. It was a {adjective2} discovery! 
        With a {noun2} in hand, {name} began to {verb} in the middle of the {place}. 
        Soon, a {number}-foot {noun1} appeared and tried to stop {name} from {verb}ing!
        It was a wild day full of surprises.
        """,

        """
        {name} had always wanted to visit {place}, and today was the day! They packed a {adjective1} bag with a {noun1}, 
        a {noun2}, and a {number}-foot rope. Upon reaching {place}, {name} noticed a {adjective2} creature lurking nearby. 
        {name} decided to {verb} to the creature and found it was friendly. Together, they explored the area and had an unforgettable time.
        """
    ]
    return random.choice(templates)

# Function to gather user inputs
def gather_user_inputs():
    """Collect inputs from the user."""
    print("\n🌟 Let's fill in the blanks for your Mad Libs story! 🌟")

    name = get_input("Enter a name: ")
    adjective1 = get_input("Enter an adjective: ")
    adjective2 = get_input("Enter another adjective: ")
    noun1 = get_input("Enter a noun: ")
    verb = get_input("Enter a verb (action word): ")
    place = get_input("Enter a place: ")
    noun2 = get_input("Enter another noun: ")
    number = get_input("Enter a number: ", int)

    return name, adjective1, adjective2, noun1, verb, place, noun2, number

# Function to create and display the Mad Libs story
def create_mad_lib(name, adjective1, adjective2, noun1, verb, place, noun2, number):
    """Create and display the story based on user inputs."""
    story_template = get_story_template()

    story = story_template.format(
        name=name, 
        adjective1=adjective1, 
        adjective2=adjective2, 
        noun1=noun1, 
        verb=verb, 
        place=place, 
        noun2=noun2, 
        number=number
    )

    print("\n🎉 Here is your Mad Libs story: 🎉")
    print("-------------------------------------------------")
    print(story)
    print("-------------------------------------------------\n")

# Main function to run the Mad Libs game
def main():
    print("Welcome to the **Mad Libs Story Generator!** 🎭")
    print("=========================================")

    # Gather inputs from the user
    name, adjective1, adjective2, noun1, verb, place, noun2, number = gather_user_inputs()

    # Create and display the Mad Libs story
    create_mad_lib(name, adjective1, adjective2, noun1, verb, place, noun2, number)

    # Option to play again
    play_again = get_input("Would you like to create another story? (yes/no): ").lower()
    if play_again == "yes":
        main()  # Restart the game
    else:
        print("\n✨ Thanks for playing! Keep being creative! ✨")

# Run the program
if __name__ == "__main__":
    main()