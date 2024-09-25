import sys
from platform import system, architecture
from get_addons import get_addons_links

version = "v1.0.2"

def display_menu():
    print(
        f"\n{'=' * 35}\n"
        f"LinkYeeter {version}, {system()} ({architecture()[0]})\n"
        f"{'=' * 35}\n"
        "Select an option:\n"
        "1. Get addons links\n"
        "2. Exit\n"
    )

def handle_choice(choice):
    options = {
        "1": get_addons_links,
        "2": sys.exit
    }

    if choice in options:
        options[choice]()
    else:
        print("Please enter a number from 1 to 2.")

def main():
    try:
        while True:
            display_menu()
            choice = input("Enter your choice (1-2): ").strip()
            handle_choice(choice)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)

if __name__ == "__main__":
    main()
