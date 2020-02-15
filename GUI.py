"""
:author: Ryan Nicholas
:date: February 14, 2020
:description: This is our GUI code
"""
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

if __name__ == '__main__':
    def open_file():
        i = 0

    def send():
        i = 0

    # Creates window
    window = tk.Tk()
    window.title("DeepFakeDetection")

    # Creates items in window
    tk.Label(window, text = "Select File:").grid(row = 0, columnspan = 3)
    tk.Entry(window).grid(row = 1)
    tk.Button(window, text = "Browse", command = open_file).grid(row = 1, column = 2)
    tk.Button(window, text = "Submit", command = send).grid(row = 2, column = 0, columnspan = 3)

    progress = Progressbar()
    window.mainloop()
