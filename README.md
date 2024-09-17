# Vermeil's Addon Link Fetcher (VALF)

**VALF** is a command-line tool designed to simplify the process of fetching addon links from Steam workshop collections. Especially useful for players who use SteamCMD, third-party programs, or other tools to manage their addons.

## Features

- 🖥️ **Cross-Platform:** Works on Windows, macOS, and Linux.
- 🌐 **Steam Collection Scraping:** Extracts all addon links from a given Steam workshop collection URL.
- 📄 **Saves Links to File:** Automatically saves extracted links to a text file.
- 🛠️ **Easy to Use:** A simple command-line interface.

## Requirements

| Operating System | Supported Versions                                       | Architecture |
|------------------|----------------------------------------------------------|--------------|
| Windows          | 11, 10, 8.1, 8                                           | 64-bit       |
| Linux            | Debian 12, Ubuntu 20.04, Fedora 38, Arch Linux, OpenSUSE | 64-bit       |
| macOS            | macOS 14, 13, 12, 11, 10.15                              | 64-bit       |

- **RAM Usage:** 20MB
- **Disk Space:** 25MB

## Installation

To install VALF, download the [latest release](https://github.com/VermeilChan/VALF/releases/latest).

- **Windows:** `VALF-1.x.x-Windows-x64.7z`
- **Linux:** `VALF-1.x.x-Linux-x64.tar.xz`
- **macOS:** `VALF-1.x.x-macOS-x64.zip`

## Usage

Upon launching the program, you will be presented with this options:

#### Option 1: Get Addon Links

- This option prompts you to enter the full link to the Steam workshop collection.
- The program scrapes the collection page, extracts all addon links, and saves them to a text file (`addon_links.txt`).

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

## Credits

- **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/):** For HTML parsing and web scraping.
- **[Requests](https://docs.python-requests.org/en/latest/):** For handling HTTP requests.
- **[PyInstaller](https://pyinstaller.org/en/stable/):** For creating standalone executables.
- **[Fake-UserAgent](https://pypi.org/project/fake-useragent/):** For generating fake user agents to avoid request blocking.
