import sys
from uuid import uuid4
from datetime import datetime
from platform import system ,architecture, win32_ver, win32_edition, freedesktop_os_release, mac_ver, machine
from get_addons import get_addons_links

version = "v1.0.2"
version += f" ({uuid4().hex[:7]})"
build_date = datetime.now().strftime("%Y-%m-%d (%A, %B %d, %Y)") # just some placeholder durning dev :)

def display_menu():
    system_info = get_os_info()
    print(
        f"{'=' * 55}\n"
        f"LinkYeeter {version}, {system_info}.\nBuild Date: {build_date}.\n"
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

def normalize_architecture(architecture):
    arch_map = {
        "x86_64": "64-bit",
        "64bit": "64-bit",
        "arm64": "Arm64"
    }
    return arch_map.get(architecture, architecture)


def get_os_info():
    sys = system()

    if sys == "Windows":
        win_version, win_release, _, _ = win32_ver()
        win_edition = win32_edition()
        arch = normalize_architecture(architecture()[0])
        return f"Windows {win_version} {win_edition} {arch}"

    elif sys == "Linux":
        try:
            distro_info = freedesktop_os_release()
            pretty_name = distro_info.get("PRETTY_NAME", "")
            version = distro_info.get("VERSION", "")
            version_id = distro_info.get("VERSION_ID", "")
            arch = normalize_architecture(architecture()[0])

            if pretty_name:
                return f"{pretty_name} {arch}"
            elif version:
                return f"{version} {arch}"
            else:
                name = distro_info.get("NAME", "Linux")
                if version_id:
                    return f"{name} {version_id} {arch}"
                else:
                    return f"{name} {arch}"

        except OSError:
            return f"Linux {normalize_architecture(architecture()[0])}"

    elif sys == "Darwin":
        mac_version = mac_ver()[0]
        arch = normalize_architecture(machine())
        return f"macOS {mac_version} {arch}"

    else:
        return "Unable to get OS information (っ °Д °;)っ"

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
