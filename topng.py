from tkinter import filedialog
from tkinter import *
import glob
from tkinter import Tk, Button
from PIL import Image

import os



def browse_button():
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)


def browse_button2():
     print(filename)
     counter = 0
     text = Label(text="DONE!")
     text.place(x=30, y=30)
     label1 = Label(root, text="Tkinter", fg="red")
     label1 = Label(root, text="Helvetica", font=("Helvetica", 24))

     global filename2
     filename2 = filedialog.askdirectory()
     folder_path.set(filename2)
     print(filename2)



     for image in glob.glob(filename + '/*.jpg'):
         counter = counter + 1
         img = Image.open(image)
         img.save(os.path.join(filename2, str(counter) + '.png'))


root = Tk()
root.geometry('400x400')
root.title('JPG to PNG')
root.configure(background='white')
folder_path = StringVar()


button2 = Button(text="Select", command=browse_button)
button2.place(x=10, y=10)


button3 = Button(text="Convert", command=browse_button2)
button3.place(x=10, y=200)

mainloop()
