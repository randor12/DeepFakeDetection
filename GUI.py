"""
:author: Ryan Nicholas, Justin Cheng, Marcus Tran
:date: February 14, 2020
:description: This is our GUI code
"""
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import Spectrogram as sp
from PIL import Image
import main


def spectrogramUpdate(name,event=None):

    return sp.main(name)


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    #spectrogramUpdate(filename)
    main.fi(filename)

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
uploadButton = tk.Button(window, text='Input', command=UploadAction, image=pho2)
uploadButton.config(height=300, width=300)
uploadButton.grid(row=0, column=1)
uploadButton.pack()
#name = filedialog.askopenfilename()
#vid.show()
holder = Text(window, height=20, width=25, font=('Times New Roman', 28), bg="black", fg="white")
scrollbar = Scrollbar(window, command=holder.yview)
holder['yscrollcommand'] = scrollbar.set
#holder.grid()
holder.pack()

window.mainloop()

    # Creates items in window

