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

img1 = cv2.imread("import\coffee1.png")
img2 = cv2.imread("import\coffee2.png")
img3 = cv2.imread("import\coffee3.png")

x1,y1 = img1.shape[1], img1.shape[0] 
x2,y2 = img2.shape[1], img1.shape[0] 
x3,y3 = img3.shape[1], img3.shape[0] 

#cv2.imshow ("img3", img3)

size =1000,500

imgresized1 = cv2.resize(img1,size)
imgresized2 = cv2.resize(img2,size)
imgresized3 = cv2.resize(img3,size)


#image modification

img_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))

img_gray1 = cv2.cvtColor(imgresized1, cv2.COLOR_BGR2GRAY)
img_blurred1 = cv2.GaussianBlur(img_gray1, (5, 5), 0)
img_thresh1 = cv2.threshold(img_blurred1, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
img_thresh11 = cv2.morphologyEx(img_thresh1, cv2.MORPH_OPEN, img_kernel)

img_gray2 = cv2.cvtColor(imgresized2, cv2.COLOR_BGR2GRAY)
img_blurred2 = cv2.GaussianBlur(img_gray2, (5, 5), 0)
img_thresh2 = cv2.threshold(img_blurred2, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
img_thresh12 = cv2.morphologyEx(img_thresh2, cv2.MORPH_OPEN, img_kernel)

img_gray3 = cv2.cvtColor(imgresized3, cv2.COLOR_BGR2GRAY)
img_blurred3 = cv2.GaussianBlur(img_gray3, (5, 5), 0)
img_thresh3 = cv2.threshold(img_blurred3, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
img_thresh13 = cv2.morphologyEx(img_thresh3, cv2.MORPH_OPEN, img_kernel)

# dilation erosion

kernel1 = np.ones((7,7),np.uint8)
kernel2 = np.ones((25,25),np.uint8)
kernel3 = np.ones((5,5),np.uint8)

dilation1 = cv2.dilate(img_thresh11,kernel1,iterations = 1)
erosion1 = cv2.erode(dilation1,kernel2,iterations = 1)
final1 = cv2.dilate(erosion1,kernel3,iterations = 1)
cv2.imwrite ('ref1.png',final1)

dilation2 = cv2.dilate(img_thresh12,kernel1,iterations = 1)
erosion2 = cv2.erode(dilation2,kernel2,iterations = 1)
final2 = cv2.dilate(erosion2,kernel3,iterations = 1)
cv2.imwrite ('ref2.png',final2)

dilation3 = cv2.dilate(img_thresh13,kernel1,iterations = 1)
erosion3 = cv2.erode(dilation3,kernel2,iterations = 1)
final3 = cv2.dilate(erosion3,kernel3,iterations = 1)
cv2.imwrite ('ref3.png',final3)


'''
text = pytesseract.image_to_string(im, lang='en')
pytesseract.
if text == "EITTE" or text == "BITTE":
    print("BITTE WÄHLEN")

elif text == "GERIT":
    print("GERÄT HEIZT AUF")

elif text == "PFLIO":
    print("PFLEGE DRÜCKEN")

else:
    print("please try again")

'''