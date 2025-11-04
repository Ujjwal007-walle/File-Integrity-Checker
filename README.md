# File Integrity Checker 🛡️

A simple Python project that monitors file changes using SHA-256 hash values.

## Features
- Calculates and stores file hash values (baseline)
- Detects modified, missing, or new files
- Uses built-in Python libraries (`hashlib`, `os`, `json`)

## How to Run
1. Put files to monitor inside the `target_files` folder.
2. Run the program:
   ```bash
   python main.py
