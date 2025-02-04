# ScanEase
 - Barcode Scanner System

## Overview
ScanEase
 is a real-time barcode scanning system built with Python. It utilizes **OpenCV**, **Pyzbar**, and **Tkinter** to provide an efficient and interactive way to scan barcodes using a webcam. The system detects barcodes in live video, decodes them, and displays the information in a user-friendly graphical interface.

## Features
- 📡 **Real-time Barcode Scanning** using a webcam
- 🔍 **Automatic Detection** and decoding of barcode types
- 🎨 **Graphical Interface** built with Tkinter
- 📏 **Visual Feedback** with a green rectangle around detected barcodes
- 🔊 **Audio Alert** upon successful barcode detection
- 🚀 **Multi-threaded Execution** for a smooth user experience

## Technologies Used
- Python
- OpenCV
- Pyzbar
- Tkinter
- Winsound (Windows only for audio alerts)

## Installation
To use ScanEase
, ensure you have Python installed and then install the required dependencies:
```sh
pip install opencv-python numpy pyzbar
```

## How to Run
1. Clone the repository or copy the script.
2. Open a terminal and navigate to the script's directory.
3. Run the script using: python barcode_scanner.py
4. Click **"Start Scan"** to begin scanning barcodes.
5. Press **'Q'** on the keyboard to exit.

## Code Breakdown
### 1. **Barcode Scanning Process**
- The script captures video frames from the webcam using OpenCV.
- It converts the frames to grayscale to improve barcode detection.
- The **Pyzbar** library decodes barcode data and type.
- A **green rectangle** highlights the detected barcode.
- The extracted information is displayed in the interface.
- A **beep sound** is played when a barcode is detected.

### 2. **Graphical Interface**
- Built with **Tkinter** for a simple and intuitive UI.
- Displays the detected barcode information.
- Features buttons for **starting and exiting** the scanner.



