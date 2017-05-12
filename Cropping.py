# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:22:52 2017

@author: Saleh Firoozabadi
"""

import numpy as np
from matplotlib import pyplot as plt
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2
from PIL import Image, ImageFilter
import PIL.ImageOps
import glob, os


#image importing and resizing

img = cv2.imread ("import\saleh.png")

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
kernel1 = np.ones((7,7),np.uint8)
kernel2 = np.ones((25,25),np.uint8)
kernel3 = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img_thresh1,kernel1,iterations = 1)
cv2.imwrite ('result\dilation.png',dilation)
erosion = cv2.erode(dilation,kernel2,iterations = 1)
cv2.imwrite ('result\erosion.png',erosion)
final = cv2.dilate(erosion,kernel3,iterations = 1)
cv2.imwrite ('final.png',final)

# Cropping the image in left and up

ixx = np.argmin(final, axis=0) # index of first zero in columns
xmin = np.min(ixx[np.nonzero(ixx)]) # the lowest nonzero value in ixx showing the lowest row # containing zero

ixy = np.argmin(final, axis=1) 
ymin = np.min(ixy[np.nonzero(ixy)]) 


# Cropping the image in right and down

flipudfinal = np.flipud(final)
flipfinal = np.fliplr(flipudfinal)

ixx2 = np.argmin(flipfinal, axis=0)
xmaxtemp = np.min(ixx2[np.nonzero(ixx2)])
xmax = x-1-xmaxtemp

ixy2 = np.argmin(flipfinal, axis=1) 
ymaxtemp = np.min(ixy2[np.nonzero(ixy2)]) 
ymax = y-1-ymaxtemp

