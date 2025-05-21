import subprocess
import os
import sys

# Get the WSI image path and output directory dynamically
if len(sys.argv) < 3:
    raise ValueError("Usage: python main_pipelines.py <wsi_image_path> <output_dir>")

wsi_image_path = sys.argv[1]  # WSI image path
output_dir = sys.argv[2]      # Output directory

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Define output files for each script
coords_file = os.path.join(output_dir, "coords_cells.csv")
real_cells_file = os.path.join(output_dir, "real_cells.csv")
features_file = os.path.join(output_dir, "features.npy")
clusters = os.path.join(output_dir, "cell_cluster_probabilities.csv")

# Define script paths
script1 = "/gpfs0/erubin/users/rivkamc/RivkaMcGowan/final_try/pipeline1v4.py"
script2 = "/gpfs0/erubin/users/rivkamc/RivkaMcGowan/final_try/pipeline2_v3.py"
script3 = "/gpfs0/erubin/users/rivkamc/RivkaMcGowan/final_try/pipeline3v5.py"
script4 = "/gpfs0/erubin/users/rivkamc/RivkaMcGowan/final_try/pipeline4v2.py"

# Run pipeline1 only if coords_cells.csv does not exist
if not os.path.exists(coords_file):
    print(f"?? Running {script1}...")
    result = subprocess.run(["python", script1, wsi_image_path, output_dir], check=False)
    if result.returncode != 0:
        print(f"? Error: {script1} failed. Stopping execution.")
        sys.exit(1)
else:
    print(f"? {coords_file} exists. Skipping {script1}.")

# Run pipeline2 only if real_cells.csv does not exist
if not os.path.exists(real_cells_file):
    print(f"?? Running {script2}...")
    result = subprocess.run(["python", script2, wsi_image_path, output_dir], check=False)
    if result.returncode != 0:
        print(f"? Error: {script2} failed. Stopping execution.")
        sys.exit(1)
else:
    print(f"? {real_cells_file} exists. Skipping {script2}.")

# Run pipeline3 only if features.npy does not exist
if not os.path.exists(features_file):
    print(f"?? Running {script3}...")
    result = subprocess.run(["python", script3, wsi_image_path, output_dir], check=False)
    if result.returncode != 0:
        print(f"? Error: {script3} failed. Stopping execution.")
        sys.exit(1)
else:
    print(f"? {features_file} exists. Skipping {script3}.")
    
# Run pipeline3 only if features.npy does not exist
if not os.path.exists(clusters):
    print(f"?? Running {script4}...")
    result = subprocess.run(["python", script4, wsi_image_path, output_dir], check=False)
    if result.returncode != 0:
        print(f"? Error: {script3} failed. Stopping execution.")
        sys.exit(1)
else:
    print(f"? {features_file} exists. Skipping {script4}.")

print("?? All necessary processing from the main completed.")
