from pathlib import Path
file_path = Path(__file__).with_name("study_note.txt")

try:
    with open(file_path) as file:
        print(file.read())
except FileNotFoundError:
    print(f"File not found: {file_path}")