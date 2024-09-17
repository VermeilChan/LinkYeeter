# Table of Contents

- [Platforms](#platforms)
- [Getting the Source Code](#getting-the-source-code)
- [Dependencies](#dependencies)
  - [Windows](#dependencies)
  - [Linux](#linux-dependencies)
  - [macOS](#dependencies)
- [Compiling](#compiling)
  - [Windows](#windows-details)
  - [Linux](#linux-details)
  - [macOS](#macos-details)

# Platforms

LinkYeeter supports the following platforms:

| Operating System | Supported Versions                                       | Architecture |
|------------------|----------------------------------------------------------|--------------|
| Windows          | 11, 10, 8.1, 8                                           | 64-bit       |
| Linux            | Debian 12, Ubuntu 20.04, Fedora 38, Arch Linux, OpenSUSE | 64-bit       |
| macOS            | macOS 14, 13, 12, 11, 10.15                              | 64-bit       |

_Windows 7 is technically supported, but you need PyInstaller 4.10._

# Getting the Source Code

- Download the zip archive from the [latest release](https://github.com/VermeilChan/LinkYeeter/releases/latest). `Source code
(zip)`

# Dependencies

You need the following to compile LinkYeeter:

- [Python](https://www.python.org/) 3.8+
- [PyInstaller](https://www.pyinstaller.org/) 6.6.0+
- [Beautiful Soup](https://pypi.org/project/beautifulsoup4/) 4.12.3+
- [Requests](https://pypi.org/project/requests/) 2.32.3+

## Linux Dependencies

For Ubuntu/Debian:
```sh
sudo apt install -y python3 python3-pip python3-venv
```
For Fedora:
```sh
sudo dnf install -y python3 python3-pip python3-virtualenv
```
For Arch:
```sh
sudo pacman -Syu --noconfirm python-pip python-virtualenv
```
For OpenSUSE:
```sh
sudo zypper install -y python3 python3-pip python3-virtualenv
```

# Compiling

## Windows

In Command Prompt:
```sh
cd VALF
py -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
pyinstaller --noconfirm --onefile --console --icon "Src/Icon/LinkYeeter.ico" --name "LinkYeeter" --clean --optimize "2" --version-file "version.txt" --add-data "Src/get_addons.py;."  "Src/cli.py"
```

## Linux

In Terminal:
```sh
cd VALF
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pyinstaller --noconfirm --onefile --console --name "LinkYeeter" --clean --optimize "2" --strip --add-data "Src/get_addons.py:."  "Src/cli.py"
```

## macOS

In Terminal:
```sh
cd VALF
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pyinstaller --noconfirm --onefile --console --name "LinkYeeter" --clean --optimize "2" --strip --add-data "Src/get_addons.py:."  "Src/cli.py"
```