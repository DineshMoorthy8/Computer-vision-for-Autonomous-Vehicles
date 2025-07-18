import torch
from pathlib import Path
import cv2

# Load trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

# Image path
img_path = "test_image.jpg"

# Inference
results = model(img_path)

# Show results
results.show()

# Save results
results.save(Path("runs/detect"))

# Print results (bounding boxes, confidences, class IDs)
print(results.pandas().xyxy[0])
