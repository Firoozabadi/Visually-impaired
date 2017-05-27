# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:22:52 2017

@author: Saleh Firoozabadi
"""

import numpy as np
from matplotlib import pyplot as plt
#from imutils.perspective import four_point_transform
#from imutils import contours
#import imutils
import cv2
from PIL import Image, ImageFilter
import PIL.ImageOps
import glob, os


#image importing and resizing

img = cv2.imread ('import\p1.jpg')

#def imageprocessing (img):
size =1000,500
imgresized = cv2.resize(img,size)
x,y = imgresized.shape[1], imgresized.shape[0] 
    
#image modification

img_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
img_gray = cv2.cvtColor(imgresized, cv2.COLOR_BGR2GRAY)
img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
img_thresh = cv2.threshold(img_blurred, 0, 255,
cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
img_thresh1 = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, img_kernel)

# dilation erosion
kernel1 = np.ones((5,5),np.uint8)
kernel2 = np.ones((40,40),np.uint8)
kernel3 = np.ones((10,10),np.uint8)
dilation = cv2.dilate(img_thresh1,kernel1,iterations = 1)
erosion = cv2.erode(dilation,kernel2,iterations = 1)
saleh = cv2.dilate(erosion,kernel3,iterations = 1)

# Cropping the image in left and up

ixx = np.argmin(saleh, axis=0) # index of first zero in columns
ymin = np.min(ixx[np.nonzero(ixx)]) # the lowest nonzero value in ixx showing the lowest row # containing zero

ixy = np.argmin(saleh, axis=1) 
xmin = np.min(ixy[np.nonzero(ixy)]) 


# Cropping the image in right and down

flipudsaleh = np.flipud(saleh)
flipsaleh = np.fliplr(flipudsaleh)

ixx2 = np.argmin(flipsaleh, axis=0)
ymaxtemp = np.min(ixx2[np.nonzero(ixx2)])
ymax = y-1-ymaxtemp

ixy2 = np.argmin(flipsaleh, axis=1) 
xmaxtemp = np.min(ixy2[np.nonzero(ixy2)]) 
xmax = x-1-xmaxtemp
   
final = saleh [ymin:ymax ,xmin:xmax]
cv2.imwrite ('1.png', final)