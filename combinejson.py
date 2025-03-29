import os
import json

# Folder containing the bgmXX directories
current_path = os.getcwd()
base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bgm")  # Change this to the correct path

all_bgm_data = []


# Loop through each JSON file in the folder
for file in os.listdir(base_folder):
    if file.endswith(".json"):
        print(f"getting json in {file}")
        file_path = os.path.join(base_folder, file)
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                # Ensure the loaded data is a list and extend the main list
                if isinstance(data, list):
                    all_bgm_data.extend(data)
                else:
                    all_bgm_data.append(data)
            except json.JSONDecodeError:
                print(f"Error reading {file_path}")

# Save the merged JSON to a new file
output_file = os.path.join(base_folder, "merged_bgm.json")
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_bgm_data, f, indent=4, ensure_ascii=False)

print(f"All JSON files merged into {output_file}")
