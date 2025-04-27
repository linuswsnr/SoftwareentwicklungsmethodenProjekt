import os
import zipfile
import json

def extract_zip_file(zip_path, extract_to):
    if not os.path.exists(zip_path):
        print(f"Zip file not found: {zip_path}")
        return False

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"File successfully extracted to: {extract_to}")
    return True

def check_dataset_contents(dataset_folder):
    if not os.path.exists(dataset_folder):
        print(f"The folder '{dataset_folder}' does not exist.")
        return False

    # Search for at least one JSON file or binary dataset
    found = False
    for root, dirs, files in os.walk(dataset_folder):
        for file in files:
            if file.endswith(".json") or file.endswith(".bin"):
                print(f"Found file: {os.path.join(root, file)}")
                found = True
                break
        if found:
            break

    if not found:
        print("No valid data files (.json or .bin) found!")
        return False

    print("Data files found and ready.")
    return True

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
    dataset_folder = os.path.join(os.getcwd(), "dataset")
    zip_file_path = os.path.join(dataset_folder, "radarscenes.zip")

    if extract_zip_file(zip_file_path, dataset_folder):
        if check_dataset_contents(dataset_folder):
            load_sample_json(dataset_folder)