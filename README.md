# Computer-vision-for-Autonomous-Vehicles
Support in setting up a hardware platform for the course" Application of machine learning in Automotive Systems" with Prof.Holger Jehle

This project explores computer vision techniques for autonomous vehicles, with an emphasis on energy-efficient object detection using PyTorch and the Sony IMX500 Smart Vision platform.
I also developed and trained a custom smartphone detection model specifically optimized to run on a Raspberry Pi.

📋 Overview
Implemented object detection for autonomous vehicles using an existing COCO dataset with PyTorch.

Optimized the detection pipeline to reduce power consumption during inference.

Integrated with the Sony IMX500 Smart Vision sensor, offloading heavy AI computation to the camera itself and reducing the workload on the Raspberry Pi.

Created and trained a custom smartphone detection model, capable of running efficiently on a Raspberry Pi.

Used Roboflow to prepare, annotate, and manage the custom dataset.

🧪 Technologies Used
🔍 PyTorch: For training and inference of YOLOv5 models.

📝 COCO Dataset: Standard dataset used to build baseline object detection.

📦 TorchScript & ONNX: For model export and optimization.

📷 Sony IMX500: Edge AI camera for offloading computation.

🍓 Raspberry Pi: Lightweight, low-power device for running inference and control.

🛠 Roboflow: For dataset creation and annotation.

🚀 Project Phases
Phase 1: Baseline Object Detection
Trained a YOLOv5 model on the COCO dataset.

Converted the model to TorchScript and ONNX for deployment.

Optimized the code to minimize power consumption and CPU load on the Raspberry Pi.

Phase 2: Edge AI with IMX500
Packaged ONNX models into .rpk files using the IMX500 SDK.

Deployed the .rpk package to the IMX500 camera.

Offloaded object detection to the camera, allowing the Raspberry Pi to focus on decision-making logic with reduced processing.

Phase 3: Custom Smartphone Detection
Collected and labeled a smartphone detection dataset using Roboflow.

Trained a YOLOv5 model on the custom dataset.

Exported the trained model (TorchScript & ONNX) for deployment on Raspberry Pi and IMX500.

Integrated the smartphone detection pipeline with webcam / camera on the Raspberry Pi.

📁 Folder Structure
bash
Copy
Edit
.
├── models/               # Trained models (best.pt, best.torchscript, best.onnx)
├── datasets/             # Dataset files and annotations
├── scripts/              # Training and inference scripts
├── imx500/               # RPK packaging files and deployment instructions
├── raspberry_pi/         # Raspberry Pi inference code
├── requirements.txt      # Python dependencies
└── README.md
⚙️ Setup & Installation
On Raspberry Pi
bash
Copy
Edit
sudo apt update
sudo apt install python3-pip
python3 -m venv yolo-venv
source yolo-venv/bin/activate

pip install torch torchvision opencv-python
pip install -r requirements.txt
Run detection with webcam:

bash
Copy
Edit
python3 detect.py --weights models/best.torchscript --source 0
On PC (for IMX500 SDK)
Download the IMX500 SDK from the Sony Developer site.

Use the provided tools to convert your ONNX model to .rpk and deploy it to the IMX500 camera.

🎯 Results
Achieved real-time object detection on Raspberry Pi with optimized power usage.

Successfully deployed detection models on IMX500, which handles AI inference internally.

Custom smartphone detection works effectively on both Raspberry Pi and IMX500.

📚 Notes
Raspberry Pi runs TorchScript or ONNX models using PyTorch/ONNX Runtime.

IMX500 requires .rpk files, which are created on a Linux PC with the IMX500 SDK.

Roboflow is used for dataset management and annotation.

📌 Future Work
Expand detection classes beyond smartphones.

Integrate vehicle control logic based on detected objects.

Explore further optimization for ultra-low-power scenarios.

🙏 Acknowledgments
Roboflow for dataset tools.

Ultralytics for YOLOv5.

Sony for the IMX500 Smart Vision Platform.


-Explore further optimization for ultra-low-power scenarios.

🙏 Acknowledgments
Roboflow for dataset tools.
Ultralytics for YOLOv5.
Sony for the IMX500 Smart Vision Platform.
