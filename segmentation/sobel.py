from tkinter import filedialog

import cv2
import matplotlib.pyplot as ppt
import numpy as np
from matplotlib.widgets import Button


class Sobel:
    path = 'home.jpg'

    def __init__(self):
        self.initUI()

    def initUI(self):
        image = cv2.imread(Sobel.path, 0)
        ppt.figure(1)

        # sobel
        sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

        laplacian = cv2.Laplacian(image, cv2.CV_64F)

        sobelxy = sobelx + sobely

        # cv2.Sobel(image, cv2.CV_64F, 1, 1, ksize=5)

        canny = cv2.Canny(image, 100, 200)

        ppt.subplot(231)
        ppt.xlabel("Original Image")
        ppt.imshow(image, cmap='gray')

        ppt.subplot(232)
        ppt.xlabel("sobel x")
        ppt.imshow(sobelx, cmap='gray')

        ppt.subplot(233)
        ppt.xlabel("sobel y")
        ppt.imshow(sobely, cmap='gray')

        ppt.subplot(234)
        ppt.xlabel("sobel xy")
        ppt.imshow(sobelxy, cmap='gray')

        ppt.subplot(235)
        ppt.xlabel("Laplacian")
        ppt.imshow(laplacian, cmap='gray')

        ppt.subplot(236)
        ppt.xlabel("Canny")
        ppt.imshow(canny, cmap='gray')

        axprev = ppt.axes([0.45, 0.005, 0.15, 0.075])
        img_bttn = Button(axprev, 'Open Image')
        img_bttn.on_clicked(lambda x: self.button_click())
        ppt.show()

    def button_click(self):
        Sobel.path = filedialog.askopenfilename(filetypes=[("Image File", '.png')])
        self.initUI()


if __name__ == '__main__':
    Sobel()
