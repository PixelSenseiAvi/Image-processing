import cv2
import matplotlib.pyplot as ppt
from matplotlib.widgets import Button
from tkinter import filedialog


class RGB:
    path = 'Cristiano.jpg'

    def __init__(self):
        self.initUI()

    def initUI(self):
        image = cv2.imread(RGB.path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ppt.figure(1)
        ppt.gray()

        red = image.copy()
        blue = image.copy()
        green = image.copy()
        blue[:, :, 0] = 0
        blue[:, :, 2] = 0
        red[:, :, 1] = 0
        red[:, :, 2] = 0
        green[:, :, 0] = 0
        green[:, :, 1] = 0

        ppt.subplot(221)
        ppt.xlabel("Original Image")
        ppt.imshow(image)

        ppt.subplot(222)
        ppt.xlabel("Red Channel")
        ppt.imshow(red)

        ppt.subplot(223)
        ppt.xlabel("Blue Channel")
        ppt.imshow(blue)

        ppt.subplot(224)
        ppt.xlabel("Green Channel")
        ppt.imshow(green)

        axprev = ppt.axes([0.45, 0.005, 0.15, 0.075])
        img_bttn = Button(axprev, 'Open Image')
        img_bttn.on_clicked(lambda x: self.button_click())
        ppt.show()

    def button_click(self):
        RGB.path = filedialog.askopenfilename(filetypes=[("Image File", '.png')])
        self.initUI()


if __name__ == '__main__':
    RGB()
