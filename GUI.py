"""
:author: Ryan Nicholas
:date: February 14, 2020
:description: This is our GUI code
"""
import tkinter as tk
from tkinter import *

if __name__ == '__main__':
    window = tk.Tk()
    window.title("DeepFakeDetection")
    tk.Label(window, text = "Select File:").grid(row = 0, columnspan = 3)
    tk.Entry(window).grid(row = 1)
    tk.Button(window, text = "Browse").grid(row = 1, column = 2)
    window.mainloop()