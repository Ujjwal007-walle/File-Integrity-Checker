# 🧩 File Integrity Checker

A **Python-based File Integrity Checker** that helps monitor changes in files using cryptographic hashes.  
It can detect unauthorized modifications by comparing files against a secure baseline.

---

## 🔍 Features
- Generates and saves file integrity baselines.
- Detects changes, deletions, or additions.
- Simple, fast, and easy to customize.

---

## 🧠 How It Works
1. On the first run, the program creates a `baseline.json` file that stores hash values for all monitored files.
2. On subsequent runs, it compares the current file states with the baseline.
3. Any modified, added, or deleted files are detected and displayed.

---

## ⚙️ Usage
Run the following command in your terminal:

```bash
python main.py

## 📁 Example Output
Modified files:
- main.py

## 🧰 Technologies Used

Python 3
hashlib
json
os

## 🧑‍💻 Author
UJJWAL KUMAR
