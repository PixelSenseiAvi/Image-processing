
# coding: utf-8

# In[1]:

import Tkinter as tk
import cv2
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageTk
import Tkconstants, tkFileDialog
import matplotlib.patches as mpatches


# In[6]:

class histograms(tk.Frame):
    
    path = "/home/cloud/Downloads/new1.jpg"
    
    def __init__(self):
        tk.Frame.__init__(self)   

        self.initUI()

    def initUI(self):
        self.master.title("")
        self.pack(fill="both", expand=True)
        
        lbl = tk.Label(self, text="RGB & gray plots")
        lbl.grid(sticky="w", pady=4, padx=5)
        
        if len(histograms.path) > 0:

            image = cv2.imread(histograms.path)
#            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
            # OpenCV represents images in BGR order; however PIL represents
            # images in RGB order, so we need to swap the channels
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
            # convert the images to PIL format...
            image = Image.fromarray(image)
            # ...and then to ImageTk format
            image = ImageTk.PhotoImage(image)
        
            label1 = tk.Label(self, image=image)
            label1.image = image
            label1.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky="nsew")
        
            ##GRAY PLOT
        
            img = cv2.imread(histograms.path)
            fig = Figure(figsize=(8,8))
            a = fig.add_subplot(111)
            a.hist(img.ravel(),150,[0,255], histtype='bar', facecolor= 'gray', align='mid')
            gray_patch = mpatches.Patch(color='gray', label='GRAY')
            a.legend(handles=[gray_patch])
            
            ##RGB PLOTS
            blue, green, red = cv2.split(img)
            
            b = fig.add_subplot(121)
            b.hist(blue.ravel(),150,[0,255], histtype='bar', facecolor= 'blue', align='mid')
            #b.set_axis_bgcolor('BLUE')
            blue_patch = mpatches.Patch(color='blue', label='BLUE')
            b.legend(handles=[blue_patch])
            
            c= fig.add_subplot(211)
            c.hist(green.ravel(),150,[0,255], histtype='bar', facecolor= 'green', align='mid')
            #c.set_axis_bgcolor('green')
            green_patch = mpatches.Patch(color='green', label='GREEN')
            c.legend(handles=[green_patch])
            
            d = fig.add_subplot(221)
            d.hist(red.ravel(),150,[0,255], histtype='bar', facecolor= 'red', align= 'mid')
            #d.set_axis_bgcolor('red')
            red_patch = mpatches.Patch(color='red', label='RED')
            d.legend(handles=[red_patch])
            
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.get_tk_widget().grid(row=1, column=3, columnspan=21, rowspan=21, sticky="EWSN")
            canvas.draw()
 

            hbtn = tk.Button(self, text = "OPEN IMAGE", command= self.button_click)
            hbtn.grid(row=5, column=1) 
        
        
    def button_click(self):
        
        histograms.path = tkFileDialog.askopenfilename(filetypes=[("Image File",'.jpg')])
        self.initUI()
        
        


# In[7]:

def main():
  
    root = tk.Tk()
    app = histograms()
    root.mainloop()  
    
if __name__ == '__main__':
    main() 


# In[ ]:


        

