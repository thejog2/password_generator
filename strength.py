# Built-in modules
# - string: gives us ready-made sets of characters (letter, digits, symbols)
import string


# This function analyses the password and returns a strength rating
def check_strength(password):
    score = 0
    # We will add checks here
    # Check length
    if len(password) >= 8:
        score += 1

    # Check for lowercase letters
    if any(char.islower() for char in password):
        score += 1

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        score += 1

    # Check for digits
    if any(char.isdigit() for char in password):
        score += 1

    # Check for symbols
    if any(char in string.punctuation for char in password):
        score += 1

    # Based on the score, we can classify the password strength
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"
    
    return score