import os
import sys
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from lightgbm import LGBMClassifier
import joblib

# Add src to sys.path so we can import radar_utils
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from radar_utils.prepare_and_merge import prepare_sequence_data

# Define the path to the Pickle dataset
PICKLE_DIR = r"C:\Users\Professional\SoftwareentwicklungsmethodenProjekt\dataset\RadarScenes_pickles"

# Load and process the data (including label merging)
df = prepare_sequence_data(pickle_dir=PICKLE_DIR)

# Extract label column first
y = df["label_id"].values

# Select only numeric features (drop all non-numeric columns)
X = df.drop(columns=["label_id"]).select_dtypes(include=["number"]).values

# Encode string class labels to numeric
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train a LightGBM classifier
model = LGBMClassifier()
model.fit(X, y_encoded)

# Predict on training data and print evaluation
y_pred = model.predict(X)
print("Classification Report (Training Data):")
print(classification_report(y_encoded, y_pred, target_names=le.classes_))

# Save model and label encoder
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/model_lightgbm.pkl")
joblib.dump(le, "models/label_encoder.pkl")



#python scripts/run_prepare.py
 #C:\Users\Professional\SoftwareentwicklungsmethodenProjekt\prepare_merge_functions>