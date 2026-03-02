import random
import string
import argparse


def generate_password(length=16, use_uppercase=True, use_digits=True, use_symbols=True):
    """Generate a random password with the given settings."""
    characters = string.ascii_lowercase

    required = []

    if use_uppercase:
        characters += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))
    if use_digits:
        characters += string.digits
        required.append(random.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        characters += symbols
        required.append(random.choice(symbols))

    if length < len(required) + 1:
        raise ValueError(f"Password length must be at least {len(required) + 1}.")

    remaining = [random.choice(characters) for _ in range(length - len(required))]
    password_list = required + remaining
    random.shuffle(password_list)

    return "".join(password_list)


def main():
    parser = argparse.ArgumentParser(description="Simple Password Generator")
    parser.add_argument("-l", "--length", type=int, default=16, help="Password length (default: 16)")
    parser.add_argument("-n", "--count", type=int, default=1, help="Number of passwords to generate (default: 1)")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    args = parser.parse_args()

    print(f"\nGenerating {args.count} password(s) of length {args.length}...\n")

    for i in range(args.count):
        pwd = generate_password(
            length=args.length,
            use_uppercase=not args.no_uppercase,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
        )
        print(f"  {i + 1}. {pwd}")

    print()


if __name__ == "__main__":
    main()
