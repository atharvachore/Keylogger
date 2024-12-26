# Keylogger
Keylogger Project
Overview
This repository contains a simple Python-based keylogger built using the pynput library. The keylogger listens to keyboard inputs and logs the keys pressed into a text file (keylog.txt). This project is intended for educational purposes only and should not be used for malicious activities.
Features
Captures all key presses on the keyboard.
Logs the captured keys into a file (keylog.txt) for later review.
Lightweight and easy to set up.
Cross-platform support (Windows, macOS, Linux) via the pynput library.
Prerequisites
Before running the keylogger, ensure you have the following installed:
Python 3.x
The pynput library
You can install pynput using pip:
bash



pip install pynput
How It Works
The script uses the pynput.keyboard.Listener class to monitor keyboard events.
When a key is pressed, the on_press function is triggered.
The key is logged into the keylog.txt file in append mode, ensuring all key presses are recorded sequentially.
Usage
Clone this repository:
bash



git clone https://github.com/your-username/keylogger-project.git
cd keylogger-project
Install the required dependencies:
bash



pip install pynput
Run the script:
bash


python keylogger.py
The key presses will be logged in the keylog.txt file in the same directory.
Code Explanation
Here’s a breakdown of the key components of the script:
on_press(key): This function is called whenever a key is pressed. It writes the key to the log file.
Listener: The pynput.keyboard.Listener class is used to listen for keyboard events. The on_press function is passed as a callback to handle key press events.
Log File: The keylog.txt file is used to store the logged keys.

Example Output
The keylog.txt file will look something like this:
javascript


'a'
'b'
'Key.space'
'c'
'd'
Disclaimer
This project is for educational purposes only. Unauthorized use of keyloggers to monitor someone else's activity without their consent is illegal and unethical. Always ensure you have proper authorization before using this tool.
License
This project is licensed under the MIT License. See the LICENSE file for details.
