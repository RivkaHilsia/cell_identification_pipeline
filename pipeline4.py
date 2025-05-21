#In this notebook, I updated the classification model
from tifffile import imread, imwrite
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import os
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import xgboost as xgb

#Special imports tp read the configuration file
import sys

sys.path.append("C:/Users/user/Documents/Hilsia_Rivka/Dream/MSc/research/usefulNotebooks/finals")
#import the configuration file
import pipelines_config_v2 as config
p = config.p

# Get the WSI image path and output directory dynamically
if len(sys.argv) < 3:
    raise ValueError("Usage: python pipeline4v2.py <wsi_image_path> <output_dir>")

wsi_img_path = sys.argv[1]  # WSI image path
output_dir = sys.argv[2]    # Output directory

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

#MAIN
feature_path = os.path.join(output_dir, "features.npy")
features = np.load(feature_path)
print(features.shape)
flat_features = features.reshape(features.shape[0], -1)  # Flatten the patches if needed
print(flat_features.shape)
# Initialize the model object
model = xgb.XGBClassifier()
# Load the saved model from JSON
classifier_path = p["classifier_path"]
model.load_model(classifier_path)
# Predict probabilities for all 25 clusters
y_prob = model.predict_proba(flat_features)
rounded_y_prob = np.round(y_prob, 4)

# Create a DataFrame with cluster probability columns
cluster_names = [f"cluster_{i}" for i in range(25)]
prob_df = pd.DataFrame(rounded_y_prob, columns=cluster_names)

# Save to CSV
# Save results inside the output directory
clusters = os.path.join(output_dir, "cell_cluster_probabilities.csv")
prob_df.to_csv(clusters)
print("Notebook 4 has run successfully")
