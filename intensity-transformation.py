
# coding: utf-8

# In[3]:

import Tkinter as tk
import cv2
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageTk
import Tkconstants, tkFileDialog
import math


# In[ ]:




# In[18]:

class histograms(tk.Frame):
    
    path = "/home/cloud/Downloads/new2.jpeg"
    path1 ="/home/cloud/Downloads/flower.jpeg"
    
    def __init__(self):
        tk.Frame.__init__(self)   

        self.initUI()

    def initUI(self):
        self.master.title("")
        self.pack(fill="both", expand=True)
        
        lbl = tk.Label(self, text="Intensity Transformation")
        lbl.grid(sticky="w", pady=4, padx=5)
        
        if len(histograms.path) > 0:

            image = cv2.imread(histograms.path)
            org_image = image
            #negative = (l(max length) - r(pixel value))
            image1 = (255 - image)


            #PIL format
            image = Image.fromarray(image)
            image1 = Image.fromarray(image1)
            #ImageTk format
            image = ImageTk.PhotoImage(image)
            image1 = ImageTk.PhotoImage(image1)
            
            label1 = tk.Label(self, image=image)
            label1.image = image
            label1.grid(row=1, column=0, columnspan=2, rowspan=2, padx=5, sticky="nsew")
            
            org_txtlbl = tk.Label(self, text="Original Image")
            org_txtlbl.grid(sticky="w", pady=4, padx=5)
            
            label2 = tk.Label(self, image=image1)
            label2.image = image1
            label2.grid(row=1, column=2, columnspan=2, rowspan=2, padx=5, sticky="nsew")
            
            neg_txtlbl = tk.Label(self, text="Negative Image")
            neg_txtlbl.grid(row=3, column =2, pady=4, padx=5)
            
            log_image= cv2.imread(histograms.path)
            c=0.6
            h = log_image.shape[0]
            w = log_image.shape[1]
            d = log_image.shape[2]
            for y in range(0, h):
                for x in range(0, w):
                    for z in range(0, d):
                    # threshold the pixel
                        log_value = math.log(1+log_image[y,x,z],2)
                        #print log_value

                        if log_value <0:
                            log_image[y,x,z] = 0
                        else :
                            log_image[y,x,z] = c*log_value
            
            #now we have got the log values of the image 
            #but it is not in the range
            temp = 255/(c*math.log(256))
            log_image = (temp*log_image).astype('uint8')
            

            #PIL format
            log_image = Image.fromarray(log_image)
            #ImageTk format
            log_image = ImageTk.PhotoImage(log_image)
            
            label3 = tk.Label(self, image=log_image)
            label3.image = log_image
            label3.grid(row=4, column=0, columnspan=2, rowspan=2, padx=5, sticky="nsew")
            
            log_txtlbl = tk.Label(self, text="Log Image, c=0.6")
            log_txtlbl.grid(sticky="w", pady=4, padx=5)
    

        hbtn = tk.Button(self, text = "OPEN IMAGE", command= self.button_click)
        hbtn.grid(row=7, column=1) 
           
        #Power-law transformation
        if len(histograms.path1) > 0:
                
            power_image = cv2.imread(histograms.path1)
            
            power_image = Image.fromarray(power_image)
            power_image = ImageTk.PhotoImage(power_image)
            label5 = tk.Label(self, image=power_image)
            label5.image = power_image
            label5.grid(row=1, column=5, columnspan=2, rowspan=2, padx=5, sticky="nsew")
            org_txtlbl = tk.Label(self, text="Original Image")
            org_txtlbl.grid(row=3,column=5, pady=4, padx=5)
                
            power_image1=cv2.imread(histograms.path1)
            power_image2=cv2.imread(histograms.path1)
            power_image3=cv2.imread(histograms.path1)
            #print power_image1
            c=1
            gamma = [0.6, 0.4, 0.3]
            h = power_image1.shape[0]
            w = power_image1.shape[1]
            d = power_image1.shape[2]
            for y in range(0, h):
                for x in range(0, w):
                    for z in range(0, d):
                        power_image1[y,x,z] = 255*c*((power_image1[y,x,z]/255.0)**gamma[0])
                        power_image2[y,x,z] = 255*c*((power_image2[y,x,z]/255.0)**gamma[1])
                        power_image3[y,x,z] = 255*c*((power_image3[y,x,z]/255.0)**gamma[2])
                        
    
                        
            power_image1 = Image.fromarray(power_image1)
            power_image1 = ImageTk.PhotoImage(power_image1)
            label6 = tk.Label(self, image=power_image1)
            label6.image = power_image1
            label6.grid(row=1, column=7, columnspan=2, rowspan=2, padx=5, sticky="nsew")
            pw1_txtlbl = tk.Label(self, text="Gamma-transformation, gamma =0.6, c=1")
            pw1_txtlbl.grid(row =3, column = 7)
        
            power_image2 = Image.fromarray(power_image2)
            power_image2 = ImageTk.PhotoImage(power_image2)
            label7 = tk.Label(self, image=power_image2)
            label7.image = power_image2
            label7.grid(row=4, column=5, columnspan=2, rowspan=2, padx=5, sticky="nsew")
            pw2_txtlbl = tk.Label(self, text="Gamma-transformation, gamma =0.4, c=1")
            pw2_txtlbl.grid(row =6, column = 5,pady=4, padx=5)
            
            power_image3 = Image.fromarray(power_image3)
            power_image3 = ImageTk.PhotoImage(power_image3)
            label8 = tk.Label(self, image=power_image3)
            label8.image = power_image3
            label8.grid(row=4, column=7, columnspan=2, rowspan=2, padx=5, sticky="nsew")
            pw3_txtlbl = tk.Label(self, text="Gamma-transformation, gamma =0.3, c=1")
            pw3_txtlbl.grid(row =6, column = 7,pady=4, padx=5)
            
        obtn = tk.Button(self, text = "OPEN IMAGE", command= self.button_click)
        obtn.grid(row=8, column=6,  pady=4, padx=5)
        
        
        histograms.path2 ="/home/cloud/Downloads/smog.jpeg"
        if len(histograms.path2) > 0:
            power_image4 = cv2.imread(histograms.path2)
            
            power_image4 = Image.fromarray(power_image4)
            power_image4 = ImageTk.PhotoImage(power_image4)
            label9 = tk.Label(self, image=power_image4)
            label9.image = power_image4
            label9.grid(row=9, column=5, columnspan=2, rowspan=2, padx=5, sticky="nsew")
            pw4_txtlbl = tk.Label(self, text="Original Image")
            pw4_txtlbl.grid(row =11, column = 5)
            
            power_image5=cv2.imread(histograms.path2)
            power_image6=cv2.imread(histograms.path2)
            power_image7=cv2.imread(histograms.path2)
            #print power_image1
            c=1
            gamma = [3, 4, 5]
            h = power_image5.shape[0]
            w = power_image5.shape[1]
            d = power_image5.shape[2]
            for y in range(0, h):
                for x in range(0, w):
                    for z in range(0, d):
                        power_image5[y,x,z] = 255*c*((power_image5[y,x,z]/255.0)**gamma[0])
                        power_image6[y,x,z] = 255*c*((power_image6[y,x,z]/255.0)**gamma[1])
                        power_image7[y,x,z] = 255*c*((power_image7[y,x,z]/255.0)**gamma[2])
                        
            power_image5 = Image.fromarray(power_image5)
            power_image5 = ImageTk.PhotoImage(power_image5)
            label10 = tk.Label(self, image=power_image5)
            label10.image = power_image5
            label10.grid(row=9, column=7, columnspan=2, rowspan=2, padx=5, sticky="nsew")
            pw5_txtlbl = tk.Label(self, text="Gamma-transformation, gamma =3, c=1")
            pw5_txtlbl.grid(row =11, column = 7)
            
            power_image6 = Image.fromarray(power_image6)
            power_image6 = ImageTk.PhotoImage(power_image6)
            label11 = tk.Label(self, image=power_image6)
            label11.image = power_image6
            label11.grid(row=12, column=5, columnspan=2, rowspan=2, padx=5, sticky="nsew")
            pw5_txtlbl = tk.Label(self, text="Gamma-transformation, gamma =4, c=1")
            pw5_txtlbl.grid(row =14, column = 5)
            
            power_image7 = Image.fromarray(power_image7)
            power_image7 = ImageTk.PhotoImage(power_image7)
            label12 = tk.Label(self, image=power_image7)
            label12.image = power_image7
            label12.grid(row=12, column=7, columnspan=2, rowspan=2, padx=5, sticky="nsew")
            pw6_txtlbl = tk.Label(self, text="Gamma-transformation, gamma =5, c=1")
            pw6_txtlbl.grid(row =14, column = 7)
        
        ohkbtn = tk.Button(self, text = "OPEN IMAGE", command= self.button_click)
        ohkbtn.grid(row=15, column=6,  pady=4, padx=5)
        
    def button_click(self,value):
        
        histograms.path = tkFileDialog.askopenfilename(filetypes=[("Image File",'.jpeg')])
        self.initUI()


# In[19]:

def main():
  
    root = tk.Tk()
    app = histograms()
    root.mainloop()  
    
if __name__ == '__main__':
    main()


# In[ ]:



