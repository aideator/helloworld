def greet(name="World"):
    """Generate a greeting message."""
    return f"Hello, {name}!"


def main():
    """Main function to demonstrate the greeting."""
    message = greet()
    print(message)
    return message


if __name__ == "__main__":
    main()