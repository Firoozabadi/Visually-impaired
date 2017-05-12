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

def imageprocessing (img):
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
    kernel1 = np.ones((7,7),np.uint8)
    kernel2 = np.ones((25,25),np.uint8)
    kernel3 = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(img_thresh1,kernel1,iterations = 1)
    erosion = cv2.erode(dilation,kernel2,iterations = 1)
    saleh = cv2.dilate(erosion,kernel3,iterations = 1)
    return [final]


img1 = cv2.imread("import\coffee1.png")
imageprocessing (img1)
cv2.imwrite ('final1.png',final)


img2 = cv2.imread("import\coffee2.png")
imageprocessing (img1)
cv2.imwrite ('final2.png',final)

img3 = cv2.imread("import\coffee3.png")
imageprocessing (img1)
cv2.imwrite ('final3.png',final)


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