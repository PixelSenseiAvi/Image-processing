from tkinter import *
import cv2
import matplotlib as mpl

mpl.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog
from scipy.signal import convolve2d as conv2

from skimage import color, restoration


class restore:
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
        self.frame3.grid(row=0, column=9)

        if len(restore.path) > 0:
            img = cv2.imread(restore.path, 0)
            min = np.minimum(img.shape[0], img.shape[1])

            img = cv2.resize(img, (min, min))
            print(img.shape)

            # psf
            h = guass2Dfilter(size=256, sigma=2)  # shape = image size
            hf = np.fft.fft2(h)
            fft_img = np.fft.fft2(img)
            G = hf * fft_img
            img1 = np.uint8(np.real(np.fft.fftshift(np.fft.ifft2(G))))

            #Adding noise
            sigma_u = (10 **(-40 / 20)) * abs(1 - 0)
            blur_noisy = img1 + sigma_u*np.random.randn(img1.shape[0])
            #blur_noisy = noisy("gauss", img1)

            #removing very low values induced due to noise
            cam_pinv = np.real(np.fft.fftshift(np.fft.ifft2((abs(hf) > 0.1) * np.fft.fft2(blur_noisy) / hf)))

            fig = Figure(figsize=(8, 8))
            a = fig.add_subplot(221)
            a.set_title("Original Image")
            a.imshow(img, cmap='gray')
            b = fig.add_subplot(222)
            b.set_title("Guassian filter")
            b.imshow(img1, cmap='gray')
            c = fig.add_subplot(223)
            c.set_title("blur and noisy")
            c.imshow(blur_noisy, cmap='gray')
            d = fig.add_subplot(224)
            d.set_title("Restore")
            d.imshow(cam_pinv, cmap='gray')

            canvas = FigureCanvasTkAgg(fig, self.frame1)
            canvas.get_tk_widget().grid(row=1, column=0, columnspan=4, rowspan=8)
            canvas.draw()

    def button_click(self, master):
        restore.path = filedialog.askopenfilename(filetypes=[("Image File", '.png')])
        self.initUI(master)


def guass2Dfilter(size, sigma=0.5):
    x, y = np.mgrid[-size // 2 + 1:size // 2 + 1, -size // 2 + 1:size // 2 + 1]
    g = np.exp(-((x ** 2 + y ** 2) / (2.0 * sigma ** 2)))

    return g / g.sum()


def noisy(noise_typ, image):
    if noise_typ == "gauss":
        row, col= image.shape
        mean = 0
        var = 0.1
        sigma = var ** 0.5
        gauss = np.random.normal(mean, sigma, (row, col))
        gauss = gauss.reshape(row, col)
        noisy = image + gauss
        return noisy
    elif noise_typ == "s&p":
        row, col, ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = np.copy(image)
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy
    elif noise_typ == "speckle":
        row, col, ch = image.shape
        gauss = np.random.randn(row, col, ch)
        gauss = gauss.reshape(row, col, ch)
        noisy = image + image * gauss
        return noisy


def main():
    root = Tk()
    root.title("Image Restoration")
    restore(root)
    root.mainloop()


if __name__ == '__main__':
    main()
