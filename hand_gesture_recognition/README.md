# Hand Gesture Recognition – Smart Presentation & Virtual Board Control

A real-time Hand Gesture Recognition System built using Python, OpenCV, and MediaPipe that allows users to control presentations, draw on screen, scroll, and navigate slides — completely hands-free without using a mouse or keyboard. This project turns your webcam into a touchless smart board controller.

## Features

- Air Cursor Control (Move mouse using index finger)
- Smart Air Pen (Draw using gesture)
- Smart Eraser (Erase using gesture)
- Next Slide Control
- Previous Slide Control
- Scroll Up
- Scroll Down
- Real-time hand landmark tracking
- Live webcam processing
- Works with both Left and Right hand
- Smooth & low-latency interaction

## Gesture Controls

- ☝- Cursor Move
- ✌- Selecting/Clicking (Air Pen) 
- 🤟- Erase 
- 👍- Next Slide 
- 🤙- Previous Slide 
- ✋- Scroll Up 
- 🤘- Scroll Down 

## Technologies Used

- Python 3
- OpenCV – Real-time video processing
- MediaPipe – Hand landmark detection
- PyAutoGUI – Mouse & keyboard automation
- NumPy

## Project Structure

Hand-Gesture-Recognition/
│
├── main.py              # Main gesture control logic
├── hand_tracker.py      # Hand tracking & landmark detection
├── gesture.py           # Gesture recognition logic
├── requirements.txt
└── README.md

## How to Run

### Clone this repository:

git clone https://github.com/your-username/hand-gesture-recognition.git

### Navigate to the project folder:

cd hand-gesture-recognition

### Install dependencies:

pip install -r requirements.txt

### Run the Project:

python main.py

### Allow camera access when prompted.

## How It Works

- Webcam captures live video.
- MediaPipe detects 21 hand landmarks.
- Finger positions are analyzed.
- Specific finger combinations are mapped to actions.
- PyAutoGUI executes mouse/keyboard actions.

## Use Cases

- Smart classroom presentations
- Touchless PPT control
- Virtual whiteboard writing
- Hygiene-friendly computer control
- Gesture-based HCI research
- Interactive demonstrations

## Future Enhancements

- Gesture smoothing for ultra-stable cursor
- Custom pen colors & thickness control
- Gesture confidence filtering
- Multi-monitor support
- Gesture analytics dashboard
- Voice + gesture hybrid control
- Multi-hand support

## Learning Outcomes

This project helps understand:

- Computer Vision fundamentals
- Hand landmark detection
- Real-time gesture recognition
- Human-Computer Interaction (HCI)
- Event-driven automation
- Practical AI integration in applications

## Challenges Solved

- Left & Right hand thumb detection correction
- Continuous drawing with proper break control
- Gesture overlap handling
- Cooldown control to prevent accidental triggers
- Smooth cursor-to-screen mapping

## Requirements

- Python 3.8+
- Webcam
- Windows / Mac / Linux

### Created by [Hariram](https://github.com/Hariram47)