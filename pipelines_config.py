#config_path: r"C:\Users\user\Documents\Hilsia_Rivka\Dream\MSc\research\usefulNotebooks\pipelines_config.yaml"

# version 1:
# created by ...

p={
  #Parameters for pipeline1
  "subset_size": [400,400,4], # this parameter define...
  "overlap":[20,20,0],
  #below is the path to save the csv file for coordinates
  #"coords_cells_csv": r"C:\Users\user\Documents\Hilsia_Rivka\Dream\MSc\research\usefulNotebooks\finals\coords_cells10.csv",
  "num_file": 1,
  "limitNumCells": 1000,

  #Parameters from pipeline2
  "k_percent": 0.2,  # Select top 20% initially
  "k_final": 51,     # Then select 51 features from those
  # Load your existing dense model
  "existing_model_path": "/gpfs0/erubin/users/rivkamc/RivkaMcGowan/final_try/supModel3_feature_model.h5",
  # Paths and directories
  #"csv_path": "/gpfs0/erubin/users/rivkamc/RivkaMcGowan/final_try/output_pipeline1v4/coords_cells100.csv",  # Update with your CSV path
  "batch_size": 96,
  "patches": "/gpfs0/erubin/users/rivkamc/RivkaMcGowan/final_try/pipelineTry1/cell_patches.npy",
  #Path to save the labels
  #"real_cells_path": r"C:\Users\user\Documents\Hilsia_Rivka\Dream\MSc\research\usefulNotebooks\finals\real_cells.csv",

  #Parameters from pipeline3
  "model_path": "/gpfs0/erubin/users/rivkamc/RivkaMcGowan/final_try/CAE_encoder_model.h5",
  "target_size": (64, 64),
  #"wsi_img_path": r"C:\Users\user\Documents\Hilsia_Rivka\Dream\MSc\research\usefulNotebooks\finals\TCGA-CR-6470-01A-01-TS1.a73d75fe-bd80-4dbb-a33b-54942d9b7057.svs",
  #"real_cell_csv": "/gpfs0/erubin/users/rivkamc/RivkaMcGowan/final_try/output_pipeline1v4/real_cells.csv/real_cells.csv",
  #Path to save the extracted features from positive cells
  #"path_features": r"C:\Users\user\Documents\Hilsia_Rivka\Dream\MSc\research\usefulNotebooks\finals\features.npy",
  
  #Parameters for pipeline 4
  "classifier_path": "/gpfs0/erubin/users/rivkamc/RivkaMcGowan/final_try/xgboost_classification_model6.json"
  

  }

