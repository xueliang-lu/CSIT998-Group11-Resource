
from ultralytics import YOLO

# Load the YOLO11 model
model = YOLO("fine tuned result/.fine_tuned_model.pt")

# Export the model to TF.js format
model.export(format="tfjs")  # creates '/yolo11n_web_model'

