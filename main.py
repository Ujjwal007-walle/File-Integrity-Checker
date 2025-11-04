import hashlib
import os
import json

BASELINE_FILE = "baseline.json"
TARGET_DIR = "target_files"  # Folder you want to monitor

def calculate_hash(file_path):
    """Calculate SHA256 hash of a file"""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def create_baseline():
    """Create a baseline with hash values of all files"""
    data = {}
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            path = os.path.join(root, file)
            data[path] = calculate_hash(path)
    with open(BASELINE_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print(f"✅ Baseline created and saved in {BASELINE_FILE}")

def check_integrity():
    """Compare current hashes with baseline"""
    if not os.path.exists(BASELINE_FILE):
        print("⚠️ No baseline found. Please create baseline first!")
        return

    with open(BASELINE_FILE, "r") as f:
        baseline = json.load(f)

    current = {}
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            path = os.path.join(root, file)
            current[path] = calculate_hash(path)

    print("\n🔍 Checking file integrity...\n")
    for path, old_hash in baseline.items():
        if path not in current:
            print(f"❌ Missing file: {path}")
        elif old_hash != current[path]:
            print(f"⚠️ Modified file: {path}")

    for path in current:
        if path not in baseline:
            print(f"🆕 New file detected: {path}")

    print("\n✅ Integrity check complete!")

def main():
    print("\n=== FILE INTEGRITY CHECKER ===")
    print("1. Create baseline")
    print("2. Check integrity")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        create_baseline()
    elif choice == "2":
        check_integrity()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    if not os.path.exists(TARGET_DIR):
        os.mkdir(TARGET_DIR)
        print(f"📁 Created folder '{TARGET_DIR}' — add files to monitor inside it.")
    main()
