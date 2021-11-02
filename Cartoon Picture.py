import cv2 #for image processing
import easygui #to open the filebox
import numpy as np #to store image
import imageio #to read image stored at particular path
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

top = tk.TK()
top.geometry("400 x 400")
top.title('Cartoonify Your Image !')
top.configure(background='white')
label=Label(top,background='#CDCDCD', font=('calibri',20,'bold'))

def upload(): # This is the filebox where we can save file paths as strings
	ImagePath = easygui.fileopenbox()
	cartoonify(ImagePath)


def cartoonify(ImagePath):
	original_image = cv2.imread(ImagePath) # Image is stored in the form of number 
	original_image = cv2.cvtColor(original_image, cv2.color_BGR2RGB) 

	if original_image is None: 
		print("Could not opne the picture.")
		sys.exit()

	resized_image = cv2.resize(original_image, (960,540)) # Resizing the image

	gray_scale_image = cv2.cvtColor(original_image, cv2.color_BGR2RGB) # Converting the image into grayscaled image

	smooth_gray_scale_image = cv2.medianBlur(gray_scale_image, 5) #Makes the Picture Blurry

	resized_image = cv2.resize(smooth_smooth_gray_scale_image, (960, 540))

	edge_image = cv2.adaptiveThreshold(smooth_gray_scale_image, 255,  #Makes a picture with only the edges
		cv2.ADAPTIVE_THRESH_MEAN_C,
		cv2.THRESH_BINARY, 9, 9)

	color_image = cv2.bilateralFilter(original_image, 9, 300, 300) # Removes the noises @ Kind of blures original image as well. 
	resized_image = cv2.resize(color_image, 960, 540) 

	cartoon_image = cv2.bitwise_and(color_image, color_image, edge_image)

	resized_image = cv2.resize(color_image, 960, 540)

def save(resized_image, ImagePath): #to save an image
	new_name = "Cartoonify Image"
	path1 = os.path.dirname(ImagePath)
	extension = os.path.splittext(ImagePath)[1]
	path = os.path.join(path1, new_name+extension)
	cv2.imwrite(path, cv2.cvtcolor(resized_image, cv2.color_BGR2RGB))
	I = "Your image is saved by name " + new_name + " at " + path
	tk.messagebox.showinfo(title = None, message = I)

	save1=Button(top,text="Save cartoon image",command=lambda: save(ImagePath, ReSized6),padx=30,pady=5)
	save1.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
	save1.pack(side=TOP,pady=50)



upload=Button(top,text="Cartoonify an Image",command=upload,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
upload.pack(side=TOP,pady=50)



top.mainloop()


































