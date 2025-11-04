# 🧩 File Integrity Checker

A Python-based File Integrity Checker that helps monitor changes in files using cryptographic hashes.  
It can detect unauthorized modifications by comparing files against a secure baseline.

## 🔍 Features
- Generates and saves file integrity baselines.
- Detects changes, deletions, or additions.
- Easy to run and customize.

## 🧠 How It Works
1. On first run, the program creates a `baseline.json` file storing hash values for all monitored files.
2. On subsequent runs, it compares the current file states with the baseline.
3. Any modified, added, or deleted files are reported.

## ⚙️ Usage
```bash
python main.py
