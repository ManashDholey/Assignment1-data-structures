import os

from pathlib import Path
script_dir = Path(__file__).resolve().parent
file_data = []
for i in range(1, 401):
    if i < 10:
        file_path = script_dir / f"data_set/bbc-fulltext/bbc/tech/00{i}.txt"
    elif i < 100:
        file_path = script_dir / f"data_set/bbc-fulltext/bbc/tech/0{i}.txt"
    else:
        file_path = script_dir / f"data_set/bbc-fulltext/bbc/tech/{i}.txt"
    print(file_path)
    if not file_path.is_file():
        print("The file does not exist.")
        continue
    else:
        with open(file_path, "r") as file:
            contents = file.read()
            file_data.append(contents)
            file.close()
print(f"Total files read: {len(file_data)}")
#print(file_data)