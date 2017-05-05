# -*- coding: utf-8 -*-
"""
Created on Fri May  5 12:02:41 2017

@author: Saleh Firoozabadi
"""

# Befor running this program, import the final.png and save the result as "tesseract"

import numpy as np
from matplotlib import pyplot as plt
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2
from PIL import Image, ImageFilter
import PIL.ImageOps
import glob, os

#import pytesseract 


text1 = open ("tesseract.txt", "r")
text = text1.read(5)

#if saleh3 == "EITTE" or "BITTE":
#    print("BITTE WÄHLEN")
#
#elif saleh3 == "GERIT" or "whatever similar":
#    print("GERÄT HEIZT AUF")
#
#elif saleh3 == "PFLIO" or "whatever similar":
#    print("PFLEGE DRÜCKEN)")
#
#else:
#    print("please try again")

if text == "EITTE":
    print("BITTE WÄHLEN")

elif text == "GERIT":
    print("GERÄT HEIZT AUF")

elif text == "PFLIO":
    print("PFLEGE DRÜCKEN)")

else:
    print("please try again")

