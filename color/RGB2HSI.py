from tkinter import filedialog

import cv2
import matplotlib.pyplot as ppt
import numpy as np
from matplotlib.widgets import Button


class RGB2HSI:
    path = 'Cristiano.jpg'

    def __init__(self):
        self.initUI()

    def initUI(self):
        image = cv2.imread(RGB2HSI.path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ppt.figure(1)
        ppt.gray()

        # Represent the image in [0-1] format
        I = np.double(image) / 255

        R = I[:, :, 0]
        G = I[:, :, 1]
        B = I[:, :, 2]

        # hue
        num = (1 / 2) * ((R - G) + (R - B))
        denom = ((R - G)**2 + ((R - B)*(G - B)))**0.5

        H = np.arccos((num/(denom+0.000001)))  # adding small value to denom to avoid / 0  error

        H[B > G] = 360 - H[B > G]
        # print(H)

        # normalize Hue values [0-1]
        H = H/360

        # saturation
        S = 1 - (3 / ((R+G+B) + 0.000001)) * np.minimum(R, G, B)

        # Intensity
        i = (1/3)*(R+G+B)

        HSI = np.zeros(image.shape)
        HSI[:, :, 0] = H
        HSI[:, :, 1] = S
        HSI[:, :, 2] = i

        # now converting HSI to RGB again
        H1 = H*360

        R1 = np.zeros(R.shape)
        B1 = np.shape(B.shape)
        G1 = np.zeros(G.shape)
        RGB1 = np.zeros(image.shape)

        ppt.subplot(121)
        ppt.xlabel("Original Image")
        ppt.imshow(image)

        ppt.subplot(122)
        ppt.xlabel("HSI Image")
        ppt.imshow(HSI)

        axprev = ppt.axes([0.45, 0.005, 0.15, 0.075])
        img_bttn = Button(axprev, 'Open Image')
        img_bttn.on_clicked(lambda x: self.button_click())
        ppt.show()

    def button_click(self):
        RGB2HSI.path = filedialog.askopenfilename(filetypes=[("Image File", '.png')])
        self.initUI()


if __name__ == '__main__':
    RGB2HSI()
