import sys
from platform import system, architecture, release
from get_addons import get_addons_links

version = "v1.0.2"

def display_menu():
    system_info = get_os_info()
    print(
        f"\n{'=' * 55}\n"
        f"LinkYeeter {version}, {system_info} ({architecture()[0]}).\nBuild Date: 2024-11-04 (Monday, November 04, 2024).\n"
        f"{'=' * 55}\n"
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

def get_linux_info():
    with open("/etc/os-release") as f:
        return dict(line.strip().split('=') for line in f)

def get_os_info():
    os_name = system()
    return f"{os_name} {release()}" if os_name != "Linux" else get_linux_info().get("PRETTY_NAME", os_name)

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
