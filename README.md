# Hand Gesture Detector

This project is a hand gesture recognition and control system that detects specific hand gestures and performs corresponding actions. The system utilizes the MediaPipe library for hand landmark tracking and PyAutoGUI for keyboard automation.

## Key Features:

* Volume Control: You can adjust the computer's volume using specific gestures such as hand closure or left/right movement.
* Customizable Configuration: The project provides the flexibility to configure new gestures and volume control commands according to your preferences.

## How It Works:

The system detects the direction of the hand (right, left, up, down) and the degree of finger closure. Based on this data, it performs specific actions such as muting the volume, increasing or decreasing the volume, or advancing slides in presentations.

## Requirements

Libraries: MediaPipe, PyAutoGUI  (pip install)

## Note:

Make sure you have the required libraries installed and a functional webcam for hand tracking input.
