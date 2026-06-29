# -------------------------------
# Password Generator
# -------------------------------

import random
import string


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generate password based on user preferences"""

    characters = ""

    if use_upper:
        characters += string.ascii_uppercase   # A-Z
    if use_lower:
        characters += string.ascii_lowercase   # a-z
    if use_digits:
        characters += string.digits            # 0-9
    if use_symbols:
        characters += string.punctuation       # special characters

    # If no option selected
    if not characters:
        return "Error: No character types selected!"

    password = ""
    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("====== PASSWORD GENERATOR ======")

    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input! Enter a number.")
        return

    print("\nSelect character types (yes/no):")

    use_upper = input("Include uppercase letters? ").lower() == "yes"
    use_lower = input("Include lowercase letters? ").lower() == "yes"
    use_digits = input("Include digits? ").lower() == "yes"
    use_symbols = input("Include symbols? ").lower() == "yes"

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    print("\nGenerated Password:")
    print(password)


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    main()
