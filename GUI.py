"""
:author: Ryan Nicholas, Justin Cheng, Marcus Tran
:date: February 14, 2020
:description: This is our GUI code
"""
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from playsound import *

if __name__ == '__main__':
    def open_file():
        i = 0 # temporary


    def send():
        i = 0 # temporary

    def play_sound(string):
        playsound(string)


    # Creates window
    window = tk.Tk()
    window.title("DeepVoice")
    window.geometry("1000x1000")

    # Creates items in window
    tk.Label(window, text="Select File:").grid(row=0, columnspan=3)
    entry = tk.Entry(window).grid(row=1)
    tk.Button(window, text="Browse", command=open_file).grid(row=1, column=2)
    tk.Button(window, text="Submit", command=send).grid(row=2, column=0, columnspan=3)
    tk.Button(window, text="Play", command=play_sound(entry)).grid(row = 3, column = 2)

    tk.Button(window, text='Quit', command=window.quit).grid(row=3, column=3)

    progress = Progressbar()
    window.mainloop()
