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


def im_processing (img):
    
    red = img[:,:,0]
    
    x,y = red.shape[1], red.shape[0]
    
    # Cropping the image in left and up
    
    ixx = np.argmax(red>100, axis=0) # index of first zero in columns
    ymin = np.min(ixx[np.nonzero(ixx)]) # the lowest nonzero value in ixx showing the lowest row # containing zero
    
    ixy = np.argmax(red>100, axis=1) 
    xmin = np.min(ixy[np.nonzero(ixy)])
    
    
    # Cropping the image in right and down
    
    flipudred = np.flipud(red)
    flipred = np.fliplr(flipudred)
    
    ixx2 = np.argmax(flipred>100, axis=0)
    ymaxtemp = np.min(ixx2[np.nonzero(ixx2)])
    ymax = y-1-ymaxtemp
    
    ixy2 = np.argmax(flipred>100, axis=1) 
    xmaxtemp = np.min(ixy2[np.nonzero(ixy2)]) 
    xmax = x-1-xmaxtemp
    
    cropped = red [ymin:ymax ,xmin:xmax]
    
    
    #----------------------------------------------------------------------
    
    size =1000,500
    imgresized = cv2.resize(cropped, size)
    
    #image modification
    
    img_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))
    #img_gray = cv2.cvtColor(imgresized, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(imgresized, (5, 5), 0)
    img_thresh = cv2.threshold(img_blurred, 0, 255,
    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    img_thresh1 = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, img_kernel)
    
    # dilation erosion
    kernel1 = np.ones((3,3),np.uint8)
    kernel2 = np.ones((20,20),np.uint8)
    kernel3 = np.ones((2,2),np.uint8)
    erosion= cv2.erode(img_thresh1,kernel2,iterations = 1)
    dilation  = cv2.dilate(erosion,kernel1,iterations = 1)

    return final;

