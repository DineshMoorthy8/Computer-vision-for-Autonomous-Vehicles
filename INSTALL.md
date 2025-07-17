This file guides users through installing and running your project.

markdown
Copy
Edit
# 🚗 Autonomous Vehicle Vision Project - Installation Guide

This project demonstrates an efficient, low-power computer vision pipeline for autonomous vehicles using PyTorch, YOLOv5, and Sony IMX500 AI sensor.
## 🔧 Requirements

- Raspberry Pi with camera module or USB camera.
- Python 3.8+
- Optional: Virtual environment (`venv` or `conda`)

---

## 📦 Installation

1️⃣ Clone the repository
bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

2️⃣ (Optional) Create virtual environment
bash
python3 -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
bash
pip install -r requirements.txt
On Raspberry Pi, also make sure to install camera drivers:

bash
sudo apt update
sudo apt install libatlas-base-dev libopenblas-dev liblapack-dev
sudo apt install libjpeg-dev zlib1g-dev
sudo apt install python3-opencv fswebcam


🚀 Running the Project

Run YOLOv5 Object Detection
bash
python detect.py --weights best.pt --source 0
--source to 0 for webcam or a path to an image/video.

Run TorchScript Model
bash
python detect_torchscript.py --weights path/to/best.torchscript --source 0
IMX500 RPK Deployment

Follow Sony’s IMX500 SDK and tools to convert your .onnx or .torchscript to .rpk and deploy it onto the AI camera.

📄 Notes
 Tested on Raspberry Pi 5 with Raspberry Pi OS Bookworm.
 Dataset created and trained using Roboflow and YOLOv5.
 Optimized to reduce power consumption and offload computation to IMX500.

📚 Resources
YOLOv5 Documentation
Roboflow
Sony IMX500
