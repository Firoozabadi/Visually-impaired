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


def imageprocessing (img):
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
    return final;


#----------------------------------------------------------------------

if __name__ == '__main__':
    
    img1 = cv2.imread ('import\p1.jpg')
    temp1 = imageprocessing (img1)
    cv2.imwrite ('processedimages\p1.jpg',temp1)
    
#    img1 = cv2.imread ('import\p2.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p2.png',temp1)
#
#    img1 = cv2.imread ('import\p3.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p3.png',temp1)
#
#    img1 = cv2.imread ('import\p4.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p4.png',temp1)
#
#    img1 = cv2.imread ('import\p5.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p5.png',temp1)
#
#    img1 = cv2.imread ('import\p6.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p6.png',temp1)
#
#    img1 = cv2.imread ('import\p7.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p7.png',temp1)
#    
#    img1 = cv2.imread ('import\p8.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p8.png',temp1)
#
#    img1 = cv2.imread ('import\p9.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p9.png',temp1)
#
#    img1 = cv2.imread ('import\p10.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p10.png',temp1)
#
#    img1 = cv2.imread ('import\p11.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p11.png',temp1)
#    
#    img1 = cv2.imread ('import\p12.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p12.png',temp1)
#    
#    img1 = cv2.imread ('import\p13.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p13.png',temp1)
#
#    img1 = cv2.imread ('import\p14.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p14.png',temp1)
#
#    img1 = cv2.imread ('import\p15.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p15.png',temp1)
#
#    img1 = cv2.imread ('import\p16.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p16.png',temp1)
#
#    img1 = cv2.imread ('import\p17.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p17.png',temp1)
#
#    img1 = cv2.imread ('import\p18.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p18.png',temp1)
#
#    img1 = cv2.imread ('import\p19.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p19.png',temp1)
#
#    img1 = cv2.imread ('import\p20.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p20.png',temp1)
#
#    img1 = cv2.imread ('import\p21.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p21.png',temp1)
#
#    img1 = cv2.imread ('import\p22.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p22.png',temp1)
#
#    img1 = cv2.imread ('import\p23.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p23.png',temp1)
#
#    img1 = cv2.imread ('import\p24.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p24.png',temp1)
#
#    img1 = cv2.imread ('import\p25.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p25.png',temp1)
#
#    img1 = cv2.imread ('import\p26.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p26.png',temp1)
#
#    img1 = cv2.imread ('import\p27.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p27.png',temp1)
#
#    img1 = cv2.imread ('import\p28.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p28.png',temp1)
#
#    img1 = cv2.imread ('import\p29.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p29.png',temp1)
#
#    img1 = cv2.imread ('import\p30.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p30.png',temp1)
#    
#    img1 = cv2.imread ('import\p31.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p31.png',temp1)
#
#    img1 = cv2.imread ('import\p32.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p32.png',temp1)
#
#    img1 = cv2.imread ('import\p33.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p33.png',temp1)
#
#    img1 = cv2.imread ('import\p34.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p34.png',temp1)
#
#    img1 = cv2.imread ('import\p35.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p35.png',temp1)
#
#    img1 = cv2.imread ('import\p36.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p36.png',temp1)
#
#    img1 = cv2.imread ('import\p37.jpg')
#    temp1 = imageprocessing (img1)
#    cv2.imwrite ('processedimages\p37.png',temp1)

