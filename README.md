# CSIT998-Group11-Resource
# Repository Overview

This repository provides resources for fine-tuning the YOLOv11s model using a custom dataset and converting the trained model for deployment in TensorFlow.js.

## Repository Structure

- **convert_result/**: Contains scripts and utilities for converting the fine-tuned model into formats suitable for deployment.
- **fine_tuned_result/**: Stores the results of the fine-tuning process, including the saved model.
- **finetunemodel.py**: The main script responsible for fine-tuning the YOLOv11s model using the provided dataset.
- **pt2tfjs.py**: A script that converts the fine-tuned PyTorch model into a TensorFlow.js compatible format.
- **YOLODataset/**: This folder contains the dataset used for fine-tuning the model, organized into separate training and validation directories, along with their corresponding labels.

## Fine-Tuning Process

1. **Dataset Structure**:
   - The `YOLODataset/` folder should contain the training and validation datasets organized in separate directories. Each directory should include images and their associated label files.

2. **Fine-Tuning the Model**:
   - Run the `finetunemodel.py` script to fine-tune the YOLOv11s model (`yolo11s.pt`) using the dataset located in the `YOLODataset/` folder.
   - Upon successful execution, the fine-tuned model will be saved as `fine_tuned_model.pt` in the `fine_tuned_result/` directory.

   ```bash
   python finetunemodel.py
3. **Model Conversion**:
After fine-tuning, run the pt2tfjs.py script to convert the fine_tuned_model.pt into a TensorFlow.js compatible format. The converted model will be saved in the fine_tuned_model_web_model/ folder, which will contain all necessary files for deployment in a web environment.
   ```bash
    python pt2tfjs.py
