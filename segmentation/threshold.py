from tkinter import filedialog

import cv2
import matplotlib.pyplot as ppt
import numpy as np
from matplotlib.widgets import Button


class Threshold:
    path = 'flower.jpg'

    def __init__(self):
        self.initUI()

    def initUI(self):
        image = cv2.imread(Threshold.path, 0)
        ppt.figure(1)

        ppt.hist(image.ravel(), 256, [0, 256])

        ppt.figure(2)

        # choosing threshold manually
        # threshold = 180
        new_image = np.where(image < 180, 0, image)

        # optimal threshold
        ret, imgf = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # adaptive threshold
        th2 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 245, 2)
        th3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 225, 2)

        ppt.subplot(231)
        ppt.xlabel("Original Gray Image")
        ppt.imshow(image, cmap='gray')

        ppt.subplot(232)
        ppt.xlabel("Manual Threshold, Th = 180")
        ppt.imshow(new_image, cmap='gray')

        ppt.subplot(233)
        ppt.xlabel("OTSU Threshold")
        ppt.imshow(imgf, cmap='gray')

        ppt.subplot(234)
        ppt.xlabel("Mean Threshold, th=245")
        ppt.imshow(th2, cmap='gray')

        ppt.subplot(236)
        ppt.xlabel("Guassian Threshold th=225")
        ppt.imshow(th3, cmap='gray')

        axprev = ppt.axes([0.45, 0.005, 0.15, 0.075])
        img_bttn = Button(axprev, 'Open Image')
        img_bttn.on_clicked(lambda x: self.button_click())
        ppt.show()

    def button_click(self):
        Threshold.path = filedialog.askopenfilename(filetypes=[("Image File", '.png')])
        self.initUI()


if __name__ == '__main__':
    Threshold()
