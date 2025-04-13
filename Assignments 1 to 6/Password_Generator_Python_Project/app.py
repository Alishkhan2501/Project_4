import random

def generate_password(chars, length):
    """Generates a single random password."""
    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("Welcome to your Password Generator!")

    # Define the set of characters to use for password generation
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*.?"

    # Input validation for number of passwords
    while True:
        try:
            number = int(input("Enter the number of passwords to generate: "))
            if number <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Input validation for password length
    while True:
        try:
            length = int(input("Enter the length of each password: "))
            if length <= 0:
                print("Please enter a positive number for password length.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generating and displaying passwords
    print("\nHere are your passwords:")
    print("=" * 40)

    passwords_list = []
    for _ in range(number):
        password = generate_password(chars, length)
        passwords_list.append(password)
        print(password)

    # Optionally, save to a file
    save_to_file = input("\nWould you like to save these passwords to a file? (yes/no): ").strip().lower()
    if save_to_file == "yes":
        filename = input("Enter the filename to save the passwords (e.g., passwords.txt): ")
        with open(filename, "w") as file:
            for password in passwords_list:
                file.write(password + "\n")
        print(f"Passwords have been saved to {filename}")

    print("\nThank you for using the Password Generator!")

if __name__ == "__main__":
    main()