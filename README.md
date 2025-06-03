# cell_identification_pipeline

This repository contains a set of pipeline scripts used for whole slide image(WSI) analysis for the purpose of cell identification and classification, along with a sample run to demonstrate the expected input/output flow. It includes all the processes from the breakdown of the wsi till the single cell images coordinates to traceback in the wsi image. It includes classification, detection, segmentation, vision transformers to build effecient models and feature extractions. 

## Scripts

- `pipeline1.py`: Preprocessing of SVS image and coordinates of cells
- `pipeline2.py`: Filtered_coordinates of cells
- `pipeline3.py`: Feature extraction
- `pipeline4.py`: classification
- `pipeline_config.py`: Shared configuration used in all scripts

## Sample_outputs
- `sample_input.svs`: Example input file
- `output_from_pipeline1.csv`: Output of pipeline1
- `output_from_pipeline2.csv`: Output of pipeline2
- `Output_from_pipeline3.npy`: Output from pipeline3
- `Output_from_pipeline4.csv`: Output from pipeline4
- `main_pipelines.py`: The terminal commands used to generate the outputs

> This is for demonstration only; execution is not included.
