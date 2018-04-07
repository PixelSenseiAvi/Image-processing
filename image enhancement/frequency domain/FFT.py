from tkinter import *

import cv2
import matplotlib as mpl

mpl.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from tkinter import filedialog


class Fourier:
    path = '/home/cloud/Desktop/fft2.png'

    def __init__(self, master):
        self.frame1 = Frame(master)
        self.frame2 = Frame(master)
        hbtn = Button(self.frame2, text="OPEN IMAGE", command=lambda: self.button_click(master))
        hbtn.pack(fill="none", expand=True)
        self.initUI(master)

    def initUI(self, master):
        self.frame1.grid(row=1, column=0)
        self.frame2.grid(row=10, column=0)

        if len(Fourier.path) > 0:
            img = cv2.imread(Fourier.path, 0)
            # computing the 2-d fourier transformation of the image
            fourier_image = np.fft.fft2(img)
            # bringing the zero components to the center
            fshift = np.fft.fftshift(fourier_image)
            magnitude_spectrum = 20 * np.log(np.abs(fshift))
            fig = Figure(figsize=(8, 8))
            fig.suptitle("Fourier Transformations")
            a = fig.add_subplot(221)

            a.imshow(img, cmap='gray')
            b = fig.add_subplot(222)

            b.imshow(magnitude_spectrum, cmap='gray')
            inv_fshift = np.fft.ifftshift(fshift)
            inverse_spectrum = 20 * np.log(np.abs(inv_fshift))
            c = fig.add_subplot(223)
            c.imshow(inverse_spectrum, cmap='gray')

            canvas = FigureCanvasTkAgg(fig, master)
            canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, rowspan=8)
            canvas.draw()

    def button_click(self, master):
        Fourier.path = filedialog.askopenfilename(filetypes=[("Image File", '.png')])
        self.initUI(master)


def main():
    root = Tk()
    root.title("Fast Fourier Transformation")
    Fourier(root)
    root.mainloop()


if __name__ == '__main__':
    main()
