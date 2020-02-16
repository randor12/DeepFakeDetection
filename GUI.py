"""
:author: Ryan Nicholas, Justin Cheng, Marcus Tran
:date: February 14, 2020
:description: This is our GUI code
"""
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image
from PredictionModel import PredictionModel

temp = None
temp2 = None

def UploadAction(event=None):
    temp2 = filedialog.askopenfilename()
    if len(temp2) > 0:
        temp = PredictionModel().predict(temp2)

        label3.config(text='Prediction: ' + str(temp))
        label2.config(text='File Path: \n' + str(temp2))

# Creates window
window = tk.Tk()
window.title("DeepVoice")
w, h = window.winfo_screenwidth()*0.9, window.winfo_screenheight()*0.9 #resizes to not completely fill window
window.geometry("%dx%d+%d+%d" % (w, h, w*.05, h*.05)) #place more in middle of screen

#resize image to better fit box
photo = Image.open('music_notes-512.png')
size = (300,300)
im2 = photo.resize(size)
im2.save('img.png', im2.format)
im2.close()
pho2 = PhotoImage(file='img.png')

canvas1 = tk.Canvas(window, width=400, height=300, relief='raised')
label3=tk.Label(window, text='Prediction: No file selected', font=('helvetica', 24))
canvas1.create_window(200, 140, window=label3)
label2 = tk.Label(window, text='File Path: Cannot show path for no file\n', font=('helvetica', 24))
canvas1.create_window(200, 190, window=label2)
canvas1.pack()

uploadButton = tk.Button(window, text='Input', command=UploadAction, image=pho2)
uploadButton.config(height=300, width=300)
uploadButton.pack()

window.mainloop()