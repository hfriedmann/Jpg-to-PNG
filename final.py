import tkinter as tk
from tkinter import filedialog
from tkinter import *
import glob
from tkinter import Button
import os
from PIL import Image
from tkinter import messagebox

# root window
root = tk.Tk()
root.geometry('250x330')
root.resizable(True, True)
root.title('Convert files')
frame = Frame(root, height=250, width=330)
frame.place(x=0, y=0)


import os
#this to add imag to onefile
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def convert_imag():
    #define features
    file_conv = {
        "height": 0,
        "width": 0,
        "type": 0,
        "location1": 0,
        "location2": 0,
        "resize": 0,
    }

    def check():
        file_conv["width"] = my_entry.get()
        file_conv["height"] = my_entry2.get()
        choice_type()
        print(file_conv)
        if file_conv["location1"] == 0 or file_conv["location2"] == 0 or file_conv["type"] == 0:
            print("pick both locations")
        else:
            if file_conv["resize"] == 0:
                print("ok. NO resisde")
            else:
                try:
                    int(file_conv["height"])
                    int(file_conv["width"])
                    print("ok. resize, int")
                except:
                    print("use only numbers")




    def browse_button():
        filename = filedialog.askdirectory()
        file_conv["location1"] = filename
        folder_path.set(filename)
        print(filename)
        if filename == "":
            print("none")
        else:
            bt_select.config(text="OK")
            print("ok")

    def browse_button2():
        filename2 = filedialog.askdirectory()
        folder_path.set(filename2)
        file_conv["location2"] = filename2
        print(filename2)
        if filename2 == "":
            print("none")
        else:
            bt_convert.config(text="OK")
            print("ok")

    def choice_type():
        if optionVar.get() == "jpg":
            file_conv["type"] = ".jpg"
        elif optionVar.get() == "gif":
            file_conv["type"] = ".gif"
        elif optionVar.get() == "png":
            file_conv["type"] = ".png"
        elif optionVar.get() == "bitmap":
            file_conv["type"] = ".bmp"
        else:
            file_conv["type"] = 1

    def isResize():
        if Checkbutton1.get() == 1:
            file_conv["resize"] = 1
            my_entry2['state'] = NORMAL
            my_entry['state'] = NORMAL
            my_entry.insert(0, '100')
            my_entry2.insert(0, '100')
        elif Checkbutton1.get() == 0:
            file_conv["resize"] = 0
            my_entry.delete(0, END)
            my_entry2.delete(0, END)
            my_entry2['state'] = DISABLED
            my_entry['state'] = DISABLED
        else:
            print("error")

    def resize():
        file_conv["width"] = my_entry.get()
        file_conv["height"] = my_entry2.get()
        choice_type()
        w = int(file_conv["width"])
        h = int(file_conv["height"])
        f = file_conv["type"]
        print(file_conv)
        counter = 0
        for image in glob.glob(file_conv["location1"] + "/*.jpg"):
            counter = counter + 1
            img = Image.open(image)
            img2 = img.resize((w, h))
            img2.save(os.path.join(str(file_conv["location2"]), str(counter) + f))
        for image in glob.glob(file_conv["location1"] + "/*.gif"):
            counter = counter + 1
            img = Image.open(image)
            img2 = img.resize((w, h))
            img2.save(os.path.join(str(file_conv["location2"]), str(counter) + f))
        for image in glob.glob(file_conv["location1"] + "/*.png"):
            counter = counter + 1
            img = Image.open(image)
            img2 = img.resize((w, h))
            img2.save(os.path.join(str(file_conv["location2"]), str(counter) + f))
        for image in glob.glob(file_conv["location1"] + "/*.bmp"):
            counter = counter + 1
            img = Image.open(image)
            img2 = img.resize((w, h))
            img2.save(os.path.join(str(file_conv["location2"]), str(counter) + f))

    def noresize():
        choice_type()
        f = file_conv["type"]
        print(file_conv)
        counter = 0
        for image in glob.glob(file_conv["location1"] + "/*.jpg"):
            counter = counter + 1
            img = Image.open(image)
            img2 = img
            img2.save(os.path.join(str(file_conv["location2"]), str(counter) + f))
        for image in glob.glob(file_conv["location1"] + "/*.gif"):
            counter = counter + 1
            img = Image.open(image)
            img2 = img
            img2.save(os.path.join(str(file_conv["location2"]), str(counter) + f))
        for image in glob.glob(file_conv["location1"] + "/*.png"):
            counter = counter + 1
            img = Image.open(image)
            img2 = img
            img2.save(os.path.join(str(file_conv["location2"]), str(counter) + f))
        for image in glob.glob(file_conv["location1"] + "/*.bmp"):
            counter = counter + 1
            img = Image.open(image)
            img2 = img
            img2.save(os.path.join(str(file_conv["location2"]), str(counter) + f))

    def converter():
        file_conv["width"] = my_entry.get()
        file_conv["height"] = my_entry2.get()
        choice_type()
        # isResize()
        print(file_conv)
        if file_conv["location1"] == 0 or file_conv["location2"] == 0 or file_conv["type"] == 0:
            print("pick both locations")
            messagebox.showerror("Error", "pick both locations")
        else:
            if file_conv["resize"] == 0:
                print("ok. NO resisde")
                noresize()
                messagebox.showinfo("Done", "Done")
            else:
                try:
                    int(file_conv["height"])
                    int(file_conv["width"])
                    print("ok. resize, int")
                    resize()
                    messagebox.showinfo("Done", "Done")
                except:
                    print("use only numbers")
                    messagebox.showerror("Error", "use only numbers")




    folder_path = StringVar()
    bt_select = Button(frame, text="in", command=browse_button)
    #bt_select.pack(fill='x', padx=5, pady=5)
    bt_convert = Button(frame, text="out", command=browse_button2)
    #bt_convert.pack(fill='x', padx=5, pady=5)
    my_entry = Entry(frame, state=DISABLED)
    #my_entry.insert(0, '10')
    #my_entry.pack(fill='x', padx=5, pady=5)
    my_entry2 = Entry(frame, state=DISABLED)
    #my_entry2.insert(0, '10')
    #my_entry2.pack(fill='x', padx=5, pady=5)

    bt_help = Button(frame, text="check", command=check)
    #bt_help.pack(fill='x', padx=50, pady=50)
    bt_converter = Button(frame, text="Convert", command=converter)
    #bt_converter.pack(fill='x', padx=50, pady=50)

    optionVar = StringVar()
    optionVar.set("jpg")
    option = OptionMenu(frame, optionVar, "jpg", "gif", "png", "bitmap")
    #option.pack(fill='x', padx=1, pady=50)

    Checkbutton1 = IntVar()
    Button1 = Checkbutton(frame, text="Resize",
                          variable=Checkbutton1,
                          onvalue=1, offvalue=0, command=isResize)
    #Button1.pack(fill='x', padx=1, pady=50)

    #possition


    info = Label(frame, text="Convert full directory")
    info.grid(row=0, column=1, columnspan=4, padx=5, pady=5, sticky="nsew", in_=frame)


    Label(frame, text="Orgin").grid(row=1, column=1, sticky="nsew")
    bt_select.grid(row=1, column=2, sticky="nsew")

    Label(frame, text="Destiny").grid(row=2, column=1, sticky="nsew")
    bt_convert.grid(row=2, column=2, sticky="nsew")

    Label(frame, text="Type").grid(row=3, column=1, sticky="nsew")
    option.grid(row=3, column=2, sticky="nsew")

    Button1.grid(row=4, column=1, sticky="nsew")

    Label(frame, text="width").grid(row=5, column=1, sticky="nsew")
    my_entry.grid(row=5, column=2, sticky="nsew")
    Label(frame, text="height").grid(row=6, column=1, sticky="nsew")
    my_entry2.grid(row=6, column=2, sticky="nsew")
    #bt_help.grid(row=7, column=1, sticky="nsew")
    bt_converter.grid(row=7, column=2, sticky="nsew")











convert_imag()
img=PhotoImage(file=resource_path("transf.gif"))
Label(frame,image=img).grid(row=9, column=2, sticky="nsew")
root.mainloop()
