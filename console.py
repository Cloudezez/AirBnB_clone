#!/usr/bin/python3

import sys

commands = {
    'help': 'Displays this help message',
    'quit': 'Exits the console'
}

def print_help():
    """
    Print the help message.
    """
    print("Documented commands (type help <topic>):")
    print("=" * 40)
    for command, description in commands.items():
        print(f"{command:5} {description}")

def main():
    """
    Main function to run the console.
    """
    if len(sys.argv) > 1:
        command = sys.stdin.read().strip()
    else:
        command = input().strip()

    if command == 'help':
        print_help()
    elif command == 'quit':
        sys.exit(0)
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()

