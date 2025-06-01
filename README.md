# CrowdGuard: Real-Time Multi-Face Detection & Crowd Alert System

CrowdGuard is a real-time face detection and crowd monitoring system designed for smart surveillance applications. Using the MTCNN deep learning model, it detects multiple faces through a webcam feed and sends signals to an Arduino controller to trigger alerts when the crowd exceeds a threshold.

---

## Features

- Real-time detection of multiple faces using MTCNN.
- Counts the number of faces in the camera frame continuously.
- Sends signals via serial communication to an Arduino when crowd size exceeds one.
- Arduino controls LED and buzzer for immediate crowd alert.
- OLED display on Arduino shows crowd status: "No" (no crowd), "Detected" (crowd present), or "Waiting...".
- Simple integration between Python and Arduino using `pyserial`.

---

## Tech Stack

- **Python 3**  
- **MTCNN** (Multi-task Cascaded Convolutional Networks) for face detection  
- **OpenCV** for video capture and image processing  
- **pyserial** for serial communication with Arduino  
- **Arduino IDE** for microcontroller programming  
- **Adafruit SSD1306 OLED** display for Arduino crowd status output  

---

## Usage

1. Run the Python script:

```bash
python examples/test.py

## System Architecture

![CrowdGuard reference Architecture]("CrowdGuard\Crowd Guard reference architecture.png")

## Setup

We recommend using **Anaconda Navigator** to manage the Python environment and dependencies efficiently.

### Steps to initialize environment:

1. Create a new conda environment (optional but recommended):

   ```bash
   conda create -n crowdguard_env python=3.8
   conda activate crowdguard_env
