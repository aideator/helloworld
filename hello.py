import argparse
import time


def greet(name="World"):
    """Generate a greeting message."""
    if name == "World":
        return "Hello World, I'm brand new"
    return f"Hello, {name}!"


def main():
    """Main function that outputs greeting at specified interval."""
    parser = argparse.ArgumentParser(description="Print greeting messages at regular intervals")
    parser.add_argument(
        "--interval", 
        type=float, 
        default=1.0,
        help="Time between messages in seconds (default: 1.0)"
    )
    args = parser.parse_args()
    
    while True:
        message = greet()
        print(message, flush=True)
        time.sleep(args.interval)


if __name__ == "__main__":    main()