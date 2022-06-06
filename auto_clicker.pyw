import pynput
import threading
import time
import random

# Set variables for click speed, start/stop toggle button and exit button
# click_delay = float(1/20)

# start_stop_button = pynput.keyboard.Key.shift_r
# exit_button = pynput.keyboard.Key.ctrl_r
start_stop_button = '+'
exit_button = '~'

click_button = pynput.mouse.Button.left
start_stop_key = pynput.keyboard.KeyCode(char=start_stop_button)
exit_key = pynput.keyboard.KeyCode(char=exit_button)
# start_stop_key = start_stop_button
# exit_key = exit_button


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super().__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                # r
                time.sleep(self.delay)
            time.sleep(0.001)


mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()
click_thread = ClickMouse(0.01*random.randrange(1, 7), click_button)
click_thread.start()


def on_key_press(key):
    print(key)
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with pynput.keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
