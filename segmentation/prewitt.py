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

        image_guassian = cv2.GaussianBlur(image, (3, 3), 0)

        # prewitt
        kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        image_prewittx = cv2.filter2D(image_guassian, -1, kernelx)
        image_prewitty = cv2.filter2D(image_guassian, -1, kernely)

        ppt.subplot(232)
        ppt.xlabel("Original Image")
        ppt.imshow(image, cmap='gray')

        ppt.subplot(234)
        ppt.xlabel("prewitt x")
        ppt.imshow(image_prewittx, cmap='gray')

        ppt.subplot(235)
        ppt.xlabel("prewitt y")
        ppt.imshow(image_prewitty, cmap='gray')

        ppt.subplot(236)
        ppt.xlabel("prewitt xy")
        ppt.imshow(image_prewittx+image_prewitty, cmap='gray')

        axprev = ppt.axes([0.45, 0.005, 0.15, 0.075])
        img_bttn = Button(axprev, 'Open Image')
        img_bttn.on_clicked(lambda x: self.button_click())
        ppt.show()

    def button_click(self):
        Sobel.path = filedialog.askopenfilename(filetypes=[("Image File", '.png')])
        self.initUI()


if __name__ == '__main__':
    Sobel()
