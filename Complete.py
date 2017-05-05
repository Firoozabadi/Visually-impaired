# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:22:52 2017

@author: Saleh Firoozabadi
"""

#import Image


#try:
#     import Image
#except ImportError:
#     from PIL import Image
#import pytesseract


import numpy as np
from matplotlib import pyplot as plt
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2
from PIL import Image, ImageFilter
import PIL.ImageOps
import glob, os

import pytesseract


#image importing and resizing

img = cv2.imread("import\coffee.png")


x,y = img.shape[1], img.shape[0] 
size =1000,500
imgresized = cv2.resize(img,size)

cv2.imwrite ("result\cofferesized.png", imgresized)

#image modification

img_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))

img_gray = cv2.cvtColor(imgresized, cv2.COLOR_BGR2GRAY)
img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
img_thresh = cv2.threshold(img_blurred, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
img_thresh1 = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, img_kernel)
cv2.imwrite ('result\img_thresh.png',img_thresh1)

# dilation erosion

kernel1 = np.ones((7,7),np.uint8)
kernel2 = np.ones((25,25),np.uint8)
kernel3 = np.ones((5,5),np.uint8)

dilation = cv2.dilate(img_thresh1,kernel1,iterations = 1)
cv2.imwrite ('result\dilation.png',dilation)
erosion = cv2.erode(dilation,kernel2,iterations = 1)
cv2.imwrite ('result\erosion.png',erosion)
final = cv2.dilate(erosion,kernel3,iterations = 1)
cv2.imwrite ('final.png',final)

im = Image.open('final.png')


text = pytesseract.image_to_string(im, lang='en')

