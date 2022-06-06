import pynput

def on_key_press(key):
    print(str(key))

with pynput.keyboard.Listener(on_press=on_key_press) as listener:
    listener.join()
