import os
import zipfile
import json

def extract_zip_file(zip_path, extract_to):
    if not os.path.exists(zip_path):
        print(f"Zip-Datei nicht gefunden: {zip_path}")
        return False

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Datei erfolgreich entpackt in: {extract_to}")
    return True

def check_dataset_contents(dataset_folder):
    if not os.path.exists(dataset_folder):
        print(f"Der Ordner '{dataset_folder}' existiert nicht.")
        return False

    # Suche nach mindestens einer JSON-Datei oder einem binären Datensatz
    found = False
    for root, dirs, files in os.walk(dataset_folder):
        for file in files:
            if file.endswith(".json") or file.endswith(".bin"):
                print(f"Gefundene Datei: {os.path.join(root, file)}")
                found = True
                break
        if found:
            break

    if not found:
        print("Keine gültigen Datendateien (.json oder .bin) gefunden!")
        return False

    print("Datendateien gefunden und bereit.")
    return True

def load_sample_json(dataset_folder):
    """Versucht, eine Beispiel-JSON-Datei zu laden und zeigt deren Inhalt."""
    for root, dirs, files in os.walk(dataset_folder):
        for file in files:
            if file.endswith(".json"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                    print(f"Beispielhafte geladene JSON-Datei: {file_path}")
                    print(f"Inhalt (erste 300 Zeichen): {str(data)[:300]}...")
                    return
                except Exception as e:
                    print(f"Fehler beim Einlesen der Datei {file_path}: {e}")
                    return
    print("Keine JSON-Datei zum Laden gefunden.")

if __name__ == "__main__":
    dataset_folder = os.path.join(os.getcwd(), "Datensatz")
    zip_file_path = os.path.join(dataset_folder, "radarscenes.zip")

    if extract_zip_file(zip_file_path, dataset_folder):
        if check_dataset_contents(dataset_folder):
            load_sample_json(dataset_folder)
