# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:22:52 2017

@author: Saleh Firoozabadi



The img has to be a matrix or an imported image using "cv2.imread (.jpg)" cmd

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

import im_processing from im_processing


#image importing and resizing

def LSQ (img):
    
    temp = im_processing (img)
    
    ref1 = cv2.imread("ref1.png")
    ref2 = cv2.imread("ref2.png")
    ref3 = cv2.imread("ref3.png")
    
    reference1 = ref1[:,:,0]
    reference2 = ref2[:,:,0]
    reference3 = ref3[:,:,0]
    
    
    #-------------------------------------------------------------
    
    temp1 = np.multiply(np.subtract(reference1, temp),np.subtract(reference1, temp))
    temp2 = np.multiply(np.subtract(reference2, temp),np.subtract(reference2, temp))
    temp3 = np.multiply(np.subtract(reference3, temp),np.subtract(reference3, temp))
    temp4 = np.multiply(np.subtract(reference4, temp),np.subtract(reference4, temp))
    
    dev1 = np.sum(temp1)
    dev2 = np.sum(temp2)
    dev3 = np.sum(temp3)
    dev4 = np.sum(temp4)
    
    print (dev1)
    print (dev2)
    print (dev3)
    print (dev4)
    
    if dev1 == min(dev1, dev2, dev3, dev4):
#        print("BITTE WÄHLEN")
        result = "BITTE WÄHLEN"
    
    elif dev2 == min(dev1, dev2, dev3, dev4):
#        print("GERÄT HEIZT AUF")
        result = "GERÄT HEIZT AUF"
        
    elif dev3 == min(dev1, dev2, dev3, dev4):
#        print("PFLEGE DRÜCKEN")
        result = "PFLEGE DRÜCKEN"
    elif dev4 == min(dev1, dev2, dev3, dev4):
#        print("PFLEGE DRÜCKEN")
        result = "Wassera tank fullen"
    else:
#        print("please try again")
        result = "PFLEGE DRÜCKEN"
        
    return result;
    

img1 = cv2.imread ("p1.jpg")
temp5 = LSQ (img1)
print temp5
