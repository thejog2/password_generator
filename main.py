import string
import random

def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    characters = ""

    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character sets selected.")

    return ''.join(random.choice(characters) for _ in range(length))


def main():
    print("=== Password Generator ===")

    length = int(input("Password length: "))

    use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include digits? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)

    print("\nGenerated password:")
    print(password)


if __name__ == "__main__":
    main()
