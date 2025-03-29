import os
import json

# Get the script directory
base_folder = os.path.dirname(os.path.abspath(__file__))

# Folder containing all `bgmXX` directories
bgm_folder = os.path.join(base_folder, "bgm")

# Dictionary to store categorized data
categorized_data = {}

for file in os.listdir(bgm_folder):
    if file.endswith(".json"):
        file_path = os.path.join(bgm_folder, file)
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)

                # Ensure data is a list
                if not isinstance(data, list):
                    data = [data]

                for item in data:
                    client_type = item.get("source", {}).get("client", "Unknown")
                    print(client_type)
                    # Add item to the corresponding category
                    if client_type not in categorized_data:
                        categorized_data[client_type] = []
                    categorized_data[client_type].append(item)
            
            except json.JSONDecodeError:
                print(f"Error reading {file_path}")

# Save each category to a separate JSON file
for client, items in categorized_data.items():
    output_file = os.path.join(base_folder, f"{client}.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=4, ensure_ascii=False)
    print(f"Saved {client}.json with {len(items)} entries.")

print("JSON files categorized successfully!")
