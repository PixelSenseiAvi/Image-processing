import cv2
import matplotlib.pyplot as ppt
from matplotlib.widgets import Button
from tkinter import filedialog
import numpy as np


class RGB:
    path = 'Cristiano.jpg'

    def __init__(self):
        self.initUI()

    def initUI(self):
        image = cv2.imread(RGB.path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ppt.figure(1)
        ppt.gray()

        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # print(gray_image)

        gray = gray_image
        (x, y) = gray_image.shape

        m = np.zeros(image.shape)
        for i in range(0, x):
            for j in range(0, y):
                if gray[i, j] >= 0 & gray[i, j] < 50:
                    m[i, j, 0] = gray[i, j] + 5
                    m[i, j, 1] = gray[i, j] + 10
                    m[i, j, 2] = gray[i, j] + 10
                if gray[i, j] >= 50 & gray[i, j] < 100:
                    m[i, j, 0] = gray[i, j] + 35
                    m[i, j, 1] = gray[i, j] + 28
                    m[i, j, 2] = gray[i, j] + 10
                if gray[i, j] >= 100 & gray[i, j] < 150:
                    m[i, j, 0] = gray[i, j] + 52
                    m[i, j, 1] = gray[i, j] + 10
                    m[i, j, 2] = gray[i, j] + 15

                if gray[i, j] >= 150 & gray[i, j] < 200:
                    m[i, j, 0] = gray[i, j] + 50
                    m[i, j, 1] = gray[i, j] + 40
                    m[i, j, 2] = gray[i, j] + 25
                if gray[i, j] >= 200 & gray[i, j] < 256:
                    m[i, j, 0] = gray[i, j] + 120
                    m[i, j, 1] = gray[i, j] + 60
                    m[i, j, 2] = gray[i, j] + 45

        m = np.uint8(m)

        ppt.subplot(121)
        ppt.xlabel("Gray Image")
        ppt.imshow(gray)

        ppt.subplot(122)
        ppt.xlabel("Pseudo Color Scheme ")
        ppt.imshow(m)

        axprev = ppt.axes([0.45, 0.005, 0.15, 0.075])
        img_bttn = Button(axprev, 'Open Image')
        img_bttn.on_clicked(lambda x: self.button_click())
        ppt.show()

    def button_click(self):
        RGB.path = filedialog.askopenfilename(filetypes=[("Image File", '.png')])
        self.initUI()


if __name__ == '__main__':
    RGB()