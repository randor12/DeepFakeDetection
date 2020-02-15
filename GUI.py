"""
:author: Ryan Nicholas, Justin Cheng, Marcus Tran
:date: February 14, 2020
:description: This is our GUI code
"""
import tkinter as tk
from tkinter import filedialog

if __name__ == '__main__':
    def open_file():
        i = 0


    def send():
        i = 0


    def UploadAction(event=None):
        filename = filedialog.askopenfilename()
        print('Selected:', filename)

    # Creates window
    window = tk.Tk()
    window.title("DeepVoice")
    w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (w, h))
    uploadButton = tk.Button(window, text='Input', command=UploadAction)
    uploadButton.pack()

    # Creates items in window

    window.mainloop()
