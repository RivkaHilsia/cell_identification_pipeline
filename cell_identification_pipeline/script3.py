#In this version of notebook, I updated the feature extraction model

import pandas as pd
import numpy as np
from tifffile import imread
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import os
import matplotlib.pyplot as plt
import imagecodecs
from tensorflow.keras.models import load_model


#Special imports tp read the configuration file
import sys

sys.path.append("C:/Users/user/Documents/Hilsia_Rivka/Dream/MSc/research/usefulNotebooks/finals")
#import the configuration file
import pipelines_config_v2 as config
p = config.p

# Get the WSI image path and output directory dynamically
if len(sys.argv) < 3:
    raise ValueError("Usage: python pipeline3v5.py <wsi_image_path> <output_dir>")

wsi_img_path = sys.argv[1]  # WSI image path
output_dir = sys.argv[2]    # Output directory

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to extract features from all valid patches (like the second block)
def extract_features(coords_df, wsi_im, target_size, model):
    patches = []
    for i, row in coords_df.iterrows():
        x_min, x_max, y_min, y_max = int(row['min x']), int(row['max x']), int(row['min y']), int(row['max y'])
        if x_min >= x_max or y_min >= y_max:
            continue
        crop = wsi_img[y_min:y_max, x_min:x_max, :]  # [:3] for RGB
        resized = tf.image.resize(crop, target_size)
        resized = tf.cast(resized, tf.float32) / 255.0
        patches.append(resized.numpy())
    patches_array = np.array(patches)
    #features = model.predict(patches_array, batch_size=64, verbose=1)
    #return features
    return patches_array

"""Main"""
# Load CAE encoder trained model from the path that is stored in config_file
#model_path = p["model_path"]
encoder = load_model("/gpfs0/erubin/users/rivkamc/RivkaMcGowan/final_try/CAE_encoder_model.h5")
#encoder = load_model(model_path)
#VGG16(weights='imagenet', include_top=False)


#wsi_img_path = p["wsi_img_path"]  #from configuration file
real_cells_csv = os.path.join(output_dir, "real_cells.csv")
coords_df = pd.read_csv(real_cells_csv)
#Loading of the wsi image once
wsi_img = imread(wsi_img_path)
print("shape of wsi image is:", wsi_img.shape)
#Extraction
#batch_size = p["batch_size"]  #from configuration file
target_size = p["target_size"]
patches = extract_features(coords_df, wsi_img, target_size, encoder)
features = encoder.predict(patches)
print("shape of the features: ", features.shape)

# Save results inside the output directory
features_file = os.path.join(output_dir, "features.npy")
np.save(features_file, features)
print("Notebook 3 has run successfully")

