import secrets
import string
import FreeSimpleGUI as sg

def generate_password(
        *,
        length=12,
        capitals=True,
        symbols=True,
        numbers=True,
):

    characters = string.ascii_lowercase
    required_groups = []

    if capitals:
        characters += string.ascii_uppercase
        required_groups.append(string.ascii_uppercase)

    if numbers:
        characters += string.digits
        required_groups.append(string.digits)

    if symbols:
        characters += "$%^&*@#!"  # Specific special characters
        required_groups.append("$%^&*@#!")

    # Generate one character from each required group
    password_chars = [secrets.choice(group) for group in required_groups]

    # Add remaining random characters from the full character list to reach desired length
    password_chars.extend(secrets.choice(characters)
                          for _ in range(length - len(password_chars)))

    # Shuffle all characters randomly
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def main():
    password = generate_password(
        length=12,
        capitals=True,
        symbols=True,
        numbers=True,
    )

    print(password)


if __name__ == "__main__":
    main()
