import torch
from ultralytics import YOLO

# Load the YOLOv8n model (nano version)
model = YOLO('yolo11s.pt')

# Fine-tune the model
# Adjust the parameters according to your needs
results = model.train(data='YOLODataset/dataset.yaml', epochs=10, imgsz=640, batch=16)

# Save the fine-tuned model
model.save('fine_tuned_model.pt')

