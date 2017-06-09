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

from im_processing import im_processing

#image importing and resizing

img1 = cv2.imread ("import\coffee2.png")

img =im_processing (img1)

cv2.imwrite ('ref.png',img)

