"""
:author: Ryan Nicholas, Justin Cheng, Marcus Tran
:date: February 14, 2020
:description: This is our GUI code
"""
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    return filename


# Creates window
window = tk.Tk()
window.title("DeepVoice")
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))

photo = PhotoImage(file = 'music_notes-512.png')

uploadButton = tk.Button(window, text='Input', command=UploadAction, image=photo)
uploadButton.config(height = 300, width = 300)
uploadButton.grid(row=0, column=1)
uploadButton.pack()

window.mainloop()

    # Creates items in window

