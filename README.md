# Smart_Survillence_For_Homes_Security_System_Using_Raspberry_Pi
-------------------------------------------------------------------
## Overview

This project implements a smart surveillance system using a Raspberry Pi 4 Model B. The system utilizes a Pi Camera Module to capture live video feeds and performs real-time face detection and recognition. The primary components include MTCNN for face detection and a FaceNet model for face recognition. The system is designed to enhance home security by identifying authorized individuals and detecting potential intruders.

## Features

- Real-time face detection and recognition
- Alerts for unrecognized faces
- High accuracy under various lighting conditions and varying distances
- Efficient processing on Raspberry Pi 4 Model B

## Hardware Requirements

- Raspberry Pi 4 Model B
- Pi Camera Module or USB Camera
- Monitor or Laptop (for initial setup and monitoring)
- Power supply for Raspberry Pi
- Wifi network

## Software Requirements

- Raspberry Pi OS (Raspbian)
- Python 3.x
- OpenCV
- pickle
- MTCNN
- FaceNet
- Additional Python libraries: numpy, scipy, imutils

## Setup Instructions

### 1. Prepare the Raspberry Pi

1. Install Raspberry Pi OS on the Raspberry Pi 4 Model B.
2. Connect the Pi Camera Module or USB Camera to the Raspberry Pi.
3. Update the system:
   ```bash
   sudo apt-get update
   sudo apt-get upgrade
   ```

### 2. Install Required Libraries

### 3. Clone the Repository

Clone the project repository to your Raspberry Pi:
```bash
git clone https://github.com/ashishbr/Smart_survillence_for_homes_Raspberry_Pi.git
cd Smart_survillence_for_homes_Raspberry_Pi
```

### 4. Configure the System

1. Prepare the dataset of home residents' face images and place them in the `Faces` directory.
2. Run the data pre-processing script to prepare the images for training:
   ```bash
   python3 detect.py
   ```

3. Train the face recognition model (if needed) or use the provided pre-trained model.

### 5. Run the Surveillance System

Start the surveillance system:
```bash
python3 MAIN_UI.py
```
and click on start surveillance
## Testing

### Details

INSTRUCTIONS FOR RUNNING:

Step 1:   First run the new.py to add a new face to the database and insert it into a folder with a person name. [uses MTCNN to detect face and capture user face alone]
Step 2:   Then run train_v2.py to train a model for the existing faces in database[using FACENET, FACIAL features are extracted]
Step 3:   Then user can run the MAIN_UI.py to open the user interface, the user can also add images from this interface; by selecting a image and then the folder with the user name. 
Step 4:  By Clicking on Start surveillance one can initiate the system. (Initially, it takes around 30 seconds to begin with the image capturing and processing)
Step 5:  Once the camera input is visible, it can detect user’s face in database (over a varied distance), if the person detected in unknown, then the alert is triggered and a frame is captured and sent to admin mobile (telegram-HOME SECURITY) using Telegram API [BotFather

