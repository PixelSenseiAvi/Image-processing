from tkinter import *
import cv2
import matplotlib as mpl

mpl.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog


class homomorphic:
    path = '/home/cloud/Desktop/TheCameraman.png'

    def __init__(self, master):
        self.frame1 = Frame(master)
        self.frame2 = Frame(master)
        self.frame3 = Frame(master)
        hbtn = Button(self.frame2, text="OPEN IMAGE", command=lambda: self.button_click(master))
        hbtn.pack(fill="none", expand=True)
        self.initUI(master)

    def initUI(self, master):
        self.frame1.grid(row=0, column=0)
        self.frame2.grid(row=10, column=0)

        if len(homomorphic.path) > 0:
            img = cv2.imread(homomorphic.path)
            img = np.float32(img)
            img = img / 255
            print(img.shape)
            M, N, dim = img.shape

            rh, rl, cutoff = 2.5, 0.5, 32

            imgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
            y, cr, cb = cv2.split(imgYCrCb)

            y_log = np.log(y + 0.01)

            y_fft = np.fft.fft2(y_log)

            y_fft_shift = np.fft.fftshift(y_fft)

            DX = N / cutoff
            G = np.ones((M, N))
            for i in range(M):
                for j in range(N):
                    G[i][j] = ((rh - rl) * (
                                1 - np.exp(-((i - M / 2) ** 2 + (j - N / 2) ** 2) / (2 * DX ** 2)))) + rl

            filter = G * y_fft_shift
            imback = np.fft.ifft2(filter)
            imback = np.uint8(np.real(imback))
            #interm = np.real(np.fft.ifft2(np.fft.ifftshift(filter)))
            #imback= np.exp(interm)

            fig = Figure(figsize=(8, 8))
            fig.suptitle("Guassian high pass filter")
            a = fig.add_subplot(221)
            a.set_title("Original Image")
            a.imshow(img, cmap='gray')
            b = fig.add_subplot(222)
            b.set_title("")
            b.imshow(imback, cmap='gray')

            canvas = FigureCanvasTkAgg(fig, self.frame1)
            canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, rowspan=8)
            canvas.draw()

    def button_click(self, master):
        homomorphic.path = filedialog.askopenfilename(filetypes=[("Image File", '.png')])
        self.initUI(master)


def main():
    root = Tk()
    root.title("High Pass Filters - Frequency Domain")
    homomorphic(root)
    root.mainloop()


if __name__ == '__main__':
    main()
