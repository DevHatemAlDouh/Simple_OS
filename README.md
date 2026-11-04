<div align="center">

# 🖥️ Simple OS

**A small command-line file management shell written in Python**

[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=flat-square&logo=windows)](https://www.microsoft.com/windows)

---

</div>

## 📖 Overview

**Simple OS** is a lightweight command-line shell prototype that provides a prompt and a set of commands for navigating directories and managing files. It is implemented in Python using the standard library.

## ✨ Features

- **📂 Directory operations:** List directory contents, change the working directory, and create or remove directories.
- **📄 File operations:** Display supported text files, create or edit files, and remove files.
- **📦 Copy and move commands:** Includes commands intended to copy and move files between directories.
- **⌨️ Interactive prompt:** Displays the entered username and current working path.

## 🛠️ Tech Stack

| Layer         | Technology                                                |
| :------------ | :-------------------------------------------------------- |
| **Language**  | Python                                                    |
| **Libraries** | Python standard library (`os`, `shutil`)                  |
| **Interface** | Command-line                                              |
| **Platform**  | Windows (the script changes to the `D:` drive at startup) |

## 📂 Project Structure

```text
Simple_OS/
└── OS.py    # Shell commands and interactive prompt
```

## 🚀 Getting Started

### Prerequisites

- Windows with a `D:` drive available
- Python 3

### Run the shell

1. Clone the repository:
   ```bash
   git clone https://github.com/DevHatemAlDouh/Simple_OS.git
   cd Simple_OS
   ```
2. Start the script:
   ```bash
   python OS.py
   ```
3. Enter a username when prompted, then enter a command at the shell prompt.

## ⌨️ Commands

| Command             | Purpose                                                               |
| :------------------ | :-------------------------------------------------------------------- |
| `ls [directory]`    | List directory contents                                               |
| `pwd`               | Print the current working directory                                   |
| `cd <directory>`    | Change to a directory                                                 |
| `cd ..`             | Move to the parent directory                                          |
| `mkdir <directory>` | Create a directory                                                    |
| `rmdir <directory>` | Remove an empty directory                                             |
| `cat <file>`        | Display a supported file                                              |
| `cat > <file>`      | Create or replace a file's contents; enter `stop` on a line to finish |
| `cat >> <file>`     | Append to a supported non-PDF file; enter `stop` on a line to finish  |
| `rm <file>`         | Remove a file                                                         |
| `cp ...`            | Copy file(s)                                                          |
| `mv ...`            | Move file(s)                                                          |

The file display/edit commands recognize `txt`, `docx`, `pptx`, `pdf`, and `xlsx` extensions, although the script handles their contents as text and does not parse office or PDF formats.

## ⚠️ Notes

- This is an early prototype, not a replacement for a system shell.
- The script switches to `D:` during startup, so it will not start as written on a system without that drive.
- Command parsing and path handling are basic; use with care, especially for file changes and removals.

## 👨‍💻 Developer

**Hatem Al-Douh**

- **GitHub:** [@DevHatemAlDouh](https://github.com/DevHatemAlDouh)
- **Repository:** [DevHatemAlDouh/Simple_OS](https://github.com/DevHatemAlDouh/Simple_OS)

<!-- {use profolio} -->
