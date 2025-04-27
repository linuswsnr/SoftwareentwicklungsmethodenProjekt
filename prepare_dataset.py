import os
import json

def load_sample_json(dataset_folder):
    """Attempts to load a sample JSON file and display its content."""
    for root, dirs, files in os.walk(dataset_folder):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                    print(f"Sample loaded JSON file: {file_path}")
                    print(f"Content (first 300 characters): {str(data)[:300]}...")
                    return
                except Exception as e:
                    print(f"Error reading the file {file_path}: {e}")
                    return
    print("No JSON file found to load.")

if __name__ == "__main__":
    dataset_folder = os.path.join(os.getcwd(), "dataset", "RadarScenes")

    if os.path.exists(dataset_folder):
        print(f"Dataset folder found: {dataset_folder}")
        load_sample_json(dataset_folder)
    else:
        print(f"Dataset folder not found: {dataset_folder}")