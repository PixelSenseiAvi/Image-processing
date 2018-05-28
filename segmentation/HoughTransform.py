from tkinter import filedialog

import cv2
import matplotlib.pyplot as ppt
import numpy as np
from matplotlib.widgets import Button


class Hough:
    path = 'sudoku.jpg'

    def __init__(self):
        self.initUI()

    def initUI(self):
        image = cv2.imread(Hough.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ppt.figure(1)

        # lower, upper threshold = 100, 150
        edges = cv2.Canny(image, 50, 150, apertureSize=3)

        # Rho, Theta threshold = 1, pi/180
        # min votes = 200
        lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

        for rho, theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * a)
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * a)

            cv2.line(image, (x1, y1), (x2, y2), color=(255, 110, 80), thickness=2)

        image1 = cv2.imread(Hough.path, 0)
        ppt.subplot(221)
        ppt.xlabel("Original Image")
        ppt.imshow(image1, cmap='gray')

        ppt.subplot(222)
        ppt.xlabel("Canny")
        ppt.imshow(edges, cmap='gray')

        ppt.subplot(223)
        ppt.xlabel("Hough Lines")
        ppt.imshow(image)

        axprev = ppt.axes([0.45, 0.005, 0.15, 0.075])
        img_bttn = Button(axprev, 'Open Image')
        img_bttn.on_clicked(lambda x: self.button_click())
        ppt.show()

    def button_click(self):
        Hough.path = filedialog.askopenfilename(filetypes=[("Image File", '.png')])
        self.initUI()


if __name__ == '__main__':
    Hough()
