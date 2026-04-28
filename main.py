# Built-in modules
# - string: gives us ready-made sets of characters (letter, digits, symbols)
# - random: lets us randomly pick character to build the password
import string
import random


# This function generates a password based on:
# - length: how long the password should be
# - use_lower: include lowercase letters
# - use_upper: include uppercase letters
# - use_digits: include numbers
# - use_symbols: include special characters
def generate_password(length, use_lower, use_upper, use_digits, use_symbols):


    # Start with an empty pool of characters
    # We'll add to this based on the user's choices
    characters = ""


    # Add character sets to the pool depending on users choices
    if use_lower:
        characters += string.ascii_lowercase  # Add lowercase letters
    if use_upper:
        characters += string.ascii_uppercase  # Add uppercase letters
    if use_digits:
        characters += string.digits  # Add numbers
    if use_symbols:
        characters += string.punctuation  # Add special characters
    # Each 'if' check whether the user wants that type of character
    # if yes, we append that set to our 'characters' string


    if not characters:
        raise ValueError("No character sets selected")
    # If the user didn't select any character types, we can't generate a password
    # So we raise an error to let them know they need to choose at least one


    password = ''.join(random.choice(characters) for _ in range(length))
    return password
    # Build the password by randomly choose characters from the pool we created
    # We do this 'length' times to get a password of the desired length


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
    password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)


    # Display the generated password to the user
    print("\nGenerated password:") # \n adds a blank line for better readability
    print(password)


# Always ensure this line is outside of the fucntion, otherwise it could crash the program
if __name__ == "__main__":
    main()
    # This line checks if the script is being run directly (instead of imported as a module)
    # If it is, it calls the main() function to start the program