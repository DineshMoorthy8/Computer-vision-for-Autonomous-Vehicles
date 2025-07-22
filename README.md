📖 Project: Application of Machine Learning in Automotive Systems
with Prof. Dr. Thomas Ewender
Support in setting up a hardware platform and implementing object detection for autonomous vehicles.

🚗 Project Overview
This project explores energy-efficient computer vision techniques for autonomous vehicles, combining the power of PyTorch, Sony IMX500 Smart Vision Sensor, and Raspberry Pi.
We designed and deployed an end-to-end object detection pipeline that:

Runs real-time detection on the Raspberry Pi for prototyping.

Leverages the Sony IMX500 sensor for edge AI computation to minimize load and power consumption on the Raspberry Pi.

Includes a custom smartphone detection model, trained specifically for this application.

The setup supports autonomous vehicle perception, emphasizing energy efficiency and embedded deployment.

🔗 Hardware & Software Toolchain
🔷 1. Model Development & Training
✅ Framework: PyTorch (YOLOv5)
✅ Dataset:

COCO dataset (for baseline training).

Custom smartphone dataset (collected & annotated using Roboflow).
✅ Training:

Trained YOLOv5 models on GPU-enabled PC.

Fine-tuned a custom smartphone detection model.

🔷 2. Model Conversion & Optimization
To run on embedded hardware, models need to be optimized:

Exported trained .pt model to:

TorchScript → runs on Raspberry Pi with PyTorch.

ONNX → runs on Raspberry Pi with ONNX Runtime or converted for IMX500.

For IMX500:

Used Sony’s IMX500 SDK to package the ONNX model into .rpk (runtime package) format.

🔷 3. Deployment Platforms
📷 Sony IMX500 Smart Vision Sensor
Performs inference on the sensor itself → outputs detection results directly (bounding boxes, labels).

Offloads heavy computation from Raspberry Pi, lowering power usage and latency.

Requires .rpk model package, deployed via IMX500 SDK.

🍓 Raspberry Pi
Runs TorchScript or ONNX models locally using Python.

Interfaces with IMX500 to receive inference results and/or visualize them.

Lightweight device, handles decision-making, logging, and user interaction.

📁 Project Folder Structure
bash
Copy
Edit
.
├── models/            # Trained models (best.pt, best.torchscript, best.onnx)
├── datasets/          # Dataset files and annotations
├── scripts/           # Training and inference scripts
├── imx500/            # RPK packaging files and deployment instructions
├── raspberry_pi/      # Raspberry Pi inference & interface code
├── requirements.txt    # Python dependencies
└── README.md
⚙️ Setup & Installation
🔷 On Raspberry Pi
bash
Copy
Edit
sudo apt update
sudo apt install python3-pip
python3 -m venv yolo-venv
source yolo-venv/bin/activate
pip install torch torchvision opencv-python
pip install -r requirements.txt
Run real-time detection with webcam:

bash
Copy
Edit
python3 detect.py --weights models/best.torchscript --source 0
🔷 On PC (for IMX500 SDK)
Install Sony IMX500 SDK (available from Sony developer portal).

Convert ONNX model → .rpk using the SDK tools.

Deploy .rpk to the IMX500 camera.

🚀 Project Phases & Achievements
📍 Phase 1: Baseline Object Detection
Trained YOLOv5 model on COCO dataset.

Converted & optimized for Raspberry Pi.

Reduced CPU load & power consumption during inference.

📍 Phase 2: Edge AI with IMX500
Converted ONNX model into .rpk.

Deployed to IMX500 → inference happens on sensor.

Raspberry Pi handles control & downstream tasks only.

📍 Phase 3: Custom Smartphone Detection
Collected & annotated a custom dataset with Roboflow.

Trained & deployed smartphone detection model.

Runs efficiently both on Raspberry Pi and IMX500.

🧪 Technologies Used
Tool/Tech	Purpose
PyTorch	Training & inference (YOLOv5)
Roboflow	Dataset preparation & annotation
COCO Dataset	Baseline object detection training
TorchScript & ONNX	Model export & optimization
Sony IMX500	On-sensor inference
Raspberry Pi	Low-power host device
OpenCV	Visualization & camera control

🎯 Results
✅ Real-time object detection on Raspberry Pi with reduced power usage.

✅ IMX500 successfully handles inference, offloading computation.

✅ Custom smartphone detection model deployed and operational on both platforms.

📚 Notes
Raspberry Pi runs TorchScript/ONNX models with PyTorch/ONNX Runtime.

IMX500 requires .rpk files created on a PC with SDK.

Roboflow is highly effective for dataset management & labeling.
