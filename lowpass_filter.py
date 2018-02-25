import cv2
from tkinter import *
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np
from tkinter import filedialog
from PIL import Image, ImageTk


class lowpass_filter:
    path = "/home/cloud/Downloads/hubble.jpg"

    # initializing the class
    # self: the first argument of every class method
    def __init__(self, master):

        self.initUI(master)


    def initUI(self, master):
        self.frame1 = Frame(master)
        self.frame2 = Frame(master)
        self.frame3 = Frame(master)
        self.frame1.pack(side = LEFT)
        self.frame2.pack(side = LEFT)
        self.frame3.pack(side = LEFT)

        if len(lowpass_filter.path) > 0:

            ##original image
            img = cv2.imread(lowpass_filter.path, 0)
            img = cv2.resize(img,(0,0), fx=0.25, fy=0.25)
            im = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(im)

            self.imglbl = Label(self.frame1, image=imgtk)
            self.imglbl.image=imgtk
            self.imglbl.grid(column=0)

            #calculating hist
            orgHist = cv2.calcHist([img], [0], None, [256], [0, 256])

            f = Figure(figsize=(3, 3))
            a = f.add_subplot(111)
            a.plot(orgHist)

            #draw canvas tkinter
            canvas = FigureCanvasTkAgg(f, self.frame1)
            canvas.show()
            canvas.get_tk_widget().grid(row= 0, column =1)


            ##average filter
            blur = cv2.blur(img, (3, 3))
            im = Image.fromarray(blur)
            imgtk = ImageTk.PhotoImage(im)

            self.imglbl = Label(self.frame2, image=imgtk)
            self.imglbl.image = imgtk
            self.imglbl.grid(column=0)

            # calculating hist
            blurHist = cv2.calcHist([blur], [0], None, [256], [0, 256])

            f = Figure(figsize=(3, 3))
            a = f.add_subplot(111)
            a.plot(blurHist)

            canvas1 = FigureCanvasTkAgg(f,self.frame2)
            canvas1.show()
            canvas1.get_tk_widget().grid(row=0, column=1)


            # nonlinear - median filter
            median = cv2.medianBlur(img, 5)
            im = Image.fromarray(median)
            imgtk = ImageTk.PhotoImage(im)

            self.imglbl2 = Label(self.frame3, image=imgtk)
            self.imglbl2.image = imgtk
            self.imglbl2.grid(column=0)

            # calculating hist
            medianHist = cv2.calcHist([median], [0], None, [256], [0, 256])

            f = Figure(figsize=(3, 3))
            a = f.add_subplot(111)
            a.plot(medianHist)

            canvas2 = FigureCanvasTkAgg(f, self.frame3)
            canvas2.show()
            canvas2.get_tk_widget().grid(row=0, column=1)

            hbtn = Button(self.frame3, text="OPEN IMAGE", command=lambda: self.button_click(master))
            hbtn.grid(row=0, column=3)

    def button_click(self, master):
            lowpass_filter.path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg')])
            if master is not None:
                self.frame1.destroy()
                self.frame2.destroy()
                self.frame3.destroy()
            self.initUI(master)

def main():
    # constructor: initializing the main window
    root = Tk()
    root.title("Smoothing Filters")

    # creating object of the class
    filterclass = lowpass_filter(root)
    # infinite loop for the main window
    root.mainloop()


# calling main method
if __name__ == '__main__':
    main()