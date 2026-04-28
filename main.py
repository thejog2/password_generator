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