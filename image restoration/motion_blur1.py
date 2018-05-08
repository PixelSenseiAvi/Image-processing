from PIL import Image
import matplotlib.pyplot as ppt
import numpy
from matplotlib.widgets import Button
from tkinter import filedialog


# PSF
def motion_process(len, size):
    sx, sy = size
    PSF = numpy.zeros((sy, sx))
    PSF[int(sy / 2):int(sy / 2 + 1), int(sx / 2 - len / 2):int(sx / 2 + len / 2)] = 1
    print(PSF)
    return PSF / PSF.sum()  #


# motion blur
def make_blurred(input, PSF, eps):
    input_fft = numpy.fft.fft2(input)
    PSF_fft = numpy.fft.fft2(PSF) + eps
    blurred = numpy.fft.ifft2(input_fft * PSF_fft)
    blurred = numpy.abs(numpy.fft.fftshift(blurred))
    return blurred


# inverse filter
def inverse(input, PSF, eps):
    input_fft = numpy.fft.fft2(input)
    PSF_fft = numpy.fft.fft2(PSF) + eps
    result = numpy.fft.ifft2(input_fft / PSF_fft)
    result = numpy.abs(numpy.fft.fftshift(result))
    return result


# wiener filter
def wiener(input, PSF, eps):
    input_fft = numpy.fft.fft2(input)
    PSF_fft = numpy.fft.fft2(PSF) + eps
    PSF_conj = numpy.conjugate(PSF_fft)
    PSF_squared = PSF_fft ** 2
    k = 0.05
    result = (PSF_conj / (PSF_squared + k)) * input_fft
    result = numpy.fft.ifft2(result)
    result = numpy.abs(numpy.fft.fftshift(result))
    return result


class motion_blur:
    path = '/home/cloud/Desktop/TheCameraman.png'

    def __init__(self):
        self.initUI()

    def initUI(self):
        image = Image.open(motion_blur.path).convert('L')
        ppt.figure(1)
        ppt.gray()
        data = numpy.asarray(image.getdata()).reshape(image.size)
        PSF = motion_process(30, data.shape)
        blurred = numpy.abs(make_blurred(data, PSF, 1e-3))

        ppt.subplot(331)
        ppt.xlabel("Motion blurred")
        ppt.imshow(blurred)

        result = inverse(blurred, PSF, 1e-3)
        ppt.subplot(332)
        ppt.xlabel("inverse deblurred")
        ppt.imshow(result)

        blurred += 0.1 * blurred.std() * numpy.random.standard_normal(blurred.shape)

        ppt.subplot(334)
        ppt.xlabel("motion & noisy blurred")
        ppt.imshow(blurred)

        result = inverse(blurred, PSF, 0.1 + 1e-3)
        ppt.subplot(335)
        ppt.xlabel("inverse deblurred")
        ppt.imshow(result)

        result = wiener(blurred, PSF, 0.1 + 1e-3)
        ppt.subplot(336)
        ppt.xlabel("wiener deblurred")
        ppt.imshow(result)

        axprev = ppt.axes([0.45, 0.005, 0.15, 0.075])
        img_bttn = Button(axprev, 'Open Image')
        img_bttn.on_clicked(lambda x: self.button_click())
        ppt.show()

    def button_click(self):
        motion_blur.path = filedialog.askopenfilename(filetypes=[("Image File", '.png')])
        self.initUI()


if __name__ == '__main__':
    motion_blur()
