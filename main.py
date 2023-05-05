from pathlib import Path

current_file= Path(__file__).resolve()
folder_path = current_file.parent

file_txt = folder_path / "file.txt"

with file_txt.open("r") as f:
    raw = f.readlines()

print(raw)