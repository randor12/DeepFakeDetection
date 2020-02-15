"""
:author: Ryan Nicholas
:date: February 14, 2020
:description: This is our GUI code
"""

import tkinter

if __name__ == '__main__':

    window = tkinter.Tk()
    window.title("DeepFakeDetection")
    label = tkinter.Label(window, text = "Select File:").pack()
    label2 = tkinter.Button(window, text = "Browse").pack()
    window.mainloop()