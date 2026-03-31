## Universal Fish-Shell installer 🐟

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[![Fish Shell](https://img.shields.io/badge/fish-4C9D4C?style=for-the-badge&logo=fish-shell&logoColor=white)](https://fishshell.com)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://www.kernel.org/)
[![Arch Linux](https://img.shields.io/badge/Arch%20Linux-1793D1?style=for-the-badge&logo=archlinux&logoColor=white)](https://archlinux.org/)
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![openSUSE](https://img.shields.io/badge/openSUSE-26939C?style=for-the-badge&logo=opensuse&logoColor=white)](https://www.opensuse.org/)
[![Solus](https://img.shields.io/badge/Solus-3F4254?style=for-the-badge&logo=solus&logoColor=white)](https://getsol.us/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge&logo=mit)](https://opensource.org/licenses/MIT)
[![Bash](https://img.shields.io/badge/shell-bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=black)](https://www.gnu.org/software/bash/)

⭐ **[Fish Shell Official Website](https://fishshell.com)**

This Python script automatically installs the Fish shell on popular Linux distributions and offers options to set it as your default shell. It's a beginner-friendly installer that handles updates, repositories, and shell changes safely.

## Features

-   Supports Arch Linux, Ubuntu, openSUSE (Tumbleweed/Leap), and Solus.
    
-   Interactive prompt: Set Fish as default shell? (Y/N).
    
-   Automatic system updates and repository additions before installation.
    
-   Clear warnings and reset tips (e.g. `chsh -s $(which bash)`).
    

## Prerequisites

-   Linux distro: Arch, Ubuntu, openSUSE, or Solus.
    
-   Python 3 installed.
    
-   Root privileges (sudo) for package managers.
    
-   Internet connexion for repositories and packages.
    

## Installation

1.  Download the script: `wget https://raw.githubusercontent.com/[your-repo]/main/install_fish.py`.
    
2.  Make it executable: `chmod +x install_fish.py`.
    
3.  Run it: `./install_fish.py`.
    
4.  Enter your distro (e.g. "Arch"), choose Y/N for default shell.
    
5.  **Restart required** for shell changes to take effect!
    

## Example Run

text

`Enter OS(Arch,Solus,OpenSuSe,Ubuntu): Arch   Arch-Fish-Installer Warning this will set your default shell to fish!   Choose an option: Y Changing the shell to Fish Remember you can always switch back by using, chsh -s (which bash) After everything is done, please restart your pc`

## Known Issues & Tips

-   openSUSE: Enter exactly "Thumbleweed" or "Leap".
    
-   Input errors? Check case sensitivity.
    
-   Unsupported distro? Extend the `enterOS_Version()` function.
    
-   Security: Review script before running (uses `subprocess` with `shell=True`).
    

## Contributing

Fork the repo, fix bugs, or add distros (e.g. Fedora). Pull requests welcome! Licence: MIT.
