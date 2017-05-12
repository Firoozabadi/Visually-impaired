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

ref1 = cv2.imread("ref1.png")
ref2 = cv2.imread("ref2.png")
ref3 = cv2.imread("ref3.png")

reference1 = ref1[:,:,0]
reference2 = ref2[:,:,0]
reference3 = ref3[:,:,0]

img = cv2.imread ("import\IMG_20170512_133233.jpg")

x,y = img.shape[1], img.shape[0] 
size =1000,500
imgresized = cv2.resize(img,size)

#image modification

img_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
img_gray = cv2.cvtColor(imgresized, cv2.COLOR_BGR2GRAY)
img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
img_thresh = cv2.threshold(img_blurred, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
img_thresh1 = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, img_kernel)

# dilation erosion

kernel1 = np.ones((5,5),np.uint8)
kernel2 = np.ones((25,25),np.uint8)
kernel3 = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img_thresh1,kernel1,iterations = 1)
erosion = cv2.erode(dilation,kernel2,iterations = 1)
newfinal = cv2.dilate(erosion,kernel3,iterations = 1)
cv2.imwrite ('newfinal.png',newfinal)

#-------------------------------------------------------------

temp1 = np.multiply(np.subtract(reference1, newfinal),np.subtract(reference1, newfinal))
temp2 = np.multiply(np.subtract(reference2, newfinal),np.subtract(reference2, newfinal))
temp3 = np.multiply(np.subtract(reference3, newfinal),np.subtract(reference3, newfinal))

saleh1 = np.sum(temp1)
saleh2 = np.sum(temp2)
saleh3 = np.sum(temp3)

print (saleh1)
print (saleh2)
print (saleh3)

if saleh1 == min(saleh1, saleh2, saleh3):
    print("BITTE WÄHLEN")

elif saleh2 == min(saleh1, saleh2, saleh3):
    print("GERÄT HEIZT AUF")

elif saleh3 == min(saleh1, saleh2, saleh3):
    print("PFLEGE DRÜCKEN")

else:
    print("please try again")
