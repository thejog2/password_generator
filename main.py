# Built-in modules
# - string: gives us ready-made sets of characters (letter, digits, symbols)
# - random: lets us randomly pick character to build the password
import string
import random

# We import the functions we need from our other files
# This allows us to keep our code organized and modular
# - generate_password: the function that creates passwords based on user preferences
# - check_strength: the function that evaluates how strong a password is
from generator import generate_password
from strength import check_strength


    # The main function handles user interaction and runs the generator
def main():
    # Display a simple title for the program
    print("=== Password Generator ===")


    # Ask the user how long the password should be
    # input() returns a string, so we convert it into an integer
    while True:
        try:
            length = int(input("Password length: "))
            break
        except ValueError:
            print("Please enter a valid number")
    # Keep asking for the password length until the user enters a valid number
    # We added this input within a loop to prevent the program from crashing if the user enters something that isn't a number


    # Ask the user which types of characters to include
    # Each answer becomes True (yes) or False (no)
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'


    # Ask how many passwords to generate
    while True:
        try:
            count = int(input("How many passwords would you like to generate? "))
            break
        except ValueError:
            print("Please enter a valid number")


    # Call the generator function with the user's choices
    print("\nGenerated Passwords:")

    # Generate and print the requested number of passwords
    # We also check the strength of each password and display it next to the password
    for i in range(count):
        password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
        strength = check_strength(password)
        print(f"{i + 1}: {password}  ({strength})")


# Always ensure this line is outside of the fucntion, otherwise it could crash the program
if __name__ == "__main__":
    main()
    # This line checks if the script is being run directly (instead of imported as a module)
    # If it is, it calls the main() function to start the program