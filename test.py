# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:22:52 2017

@author: Saleh Firoozabadi
"""

#import Image


#try:
#     import Image
#except ImportError:
#     from PIL import Image
#import pytesseract


import numpy as np
from matplotlib import pyplot as plt
from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import cv2
from PIL import Image, ImageFilter
import PIL.ImageOps
import glob, os

import pytesseract 

#from tesseract import image_to_string

#import pytesser

'''
image_file = 'img_thresh.png'
im = Image.open(image_file)
text = image_to_string(im)
text = image_file_to_string(image_file)
text = image_file_to_string(image_file, graceful_errors=True)
print ("=====output=======\n")
print (text)


# Wrappign

img = cv2.imread('.png')
rows,cols,ch = img.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]]) #input dimentions
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) #output dimentions

M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

'''

#image importing and resizing

img1 = cv2.imread("import\coffee1.png")
img2 = cv2.imread("import\coffee2.png")
img3 = cv2.imread("import\coffee3.jpg")

x1,y1 = img1.shape[1], img1.shape[0] 
x2,y2 = img2.shape[1], img1.shape[0] 
x3,y3 = img3.shape[1], img3.shape[0] 

#cv2.imshow ("img3", img3)

size =1000,500

imgresized1 = cv2.resize(img1,size)
imgresized2 = cv2.resize(img2,size)
imgresized3 = cv2.resize(img3,size)

cv2.imwrite ("result\cofferesized1.png", imgresized1)
cv2.imwrite ("result\cofferesized2.png", imgresized2)
cv2.imwrite ("result\cofferesized3.png", imgresized3)
#
size =1000,500

imgresized11 = cv2.resize(imgresized1,size)
imgresized12 = cv2.resize(imgresized2,size)
imgresized13 = cv2.resize(imgresized3,size)

cv2.imwrite ("result\cofferesized11.png", imgresized11)
cv2.imwrite ("result\cofferesized12.png", imgresized12)
cv2.imwrite ("result\cofferesized13.png", imgresized13)

img_blurred11 = cv2.GaussianBlur(imgresized11, (5, 5), 0)
img_blurred12 = cv2.GaussianBlur(imgresized12, (5, 5), 0)
img_blurred13 = cv2.GaussianBlur(imgresized13, (5, 5), 0)

cv2.imwrite ("result\img_blurred11.png", img_blurred11)
cv2.imwrite ("result\img_blurred12.png", img_blurred12)
cv2.imwrite ("result\img_blurred13.png", img_blurred13)


#image modification

img_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 5))

img_gray1 = cv2.cvtColor(imgresized11, cv2.COLOR_BGR2GRAY)
img_blurred1 = cv2.GaussianBlur(img_gray1, (5, 5), 0)
img_thresh1 = cv2.threshold(img_blurred1, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
img_thresh11 = cv2.morphologyEx(img_thresh1, cv2.MORPH_OPEN, img_kernel)
cv2.imwrite ('result\img_thresh1.png',img_thresh11)

img_gray2 = cv2.cvtColor(imgresized2, cv2.COLOR_BGR2GRAY)
img_blurred2 = cv2.GaussianBlur(img_gray2, (5, 5), 0)
img_thresh2 = cv2.threshold(img_blurred2, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
img_thresh12 = cv2.morphologyEx(img_thresh2, cv2.MORPH_OPEN, img_kernel)
cv2.imwrite ('result\img_thresh2.png',img_thresh12)

img_gray3 = cv2.cvtColor(imgresized3, cv2.COLOR_BGR2GRAY)
img_blurred3 = cv2.GaussianBlur(img_gray3, (5, 5), 0)
img_thresh3 = cv2.threshold(img_blurred3, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
img_thresh13 = cv2.morphologyEx(img_thresh3, cv2.MORPH_OPEN, img_kernel)
cv2.imwrite ('result\img_thresh.png',img_thresh2)

# dilation erosion

kernel1 = np.ones((7,7),np.uint8)
kernel2 = np.ones((25,25),np.uint8)
kernel3 = np.ones((5,5),np.uint8)

dilation1 = cv2.dilate(img_thresh11,kernel1,iterations = 1)
cv2.imwrite ('result\dilation1.png',dilation1)
erosion1 = cv2.erode(dilation1,kernel2,iterations = 1)
cv2.imwrite ('result\erosion1.png',erosion1)
final1 = cv2.dilate(erosion1,kernel3,iterations = 1)
cv2.imwrite ('result\saleh1.png',final1)

dilation2 = cv2.dilate(img_thresh12,kernel1,iterations = 1)
cv2.imwrite ('result\dilation2.png',dilation2)
erosion2 = cv2.erode(dilation2,kernel2,iterations = 1)
cv2.imwrite ('result\erosion2.png',erosion2)
final2 = cv2.dilate(erosion2,kernel3,iterations = 1)
cv2.imwrite ('result\saleh2.png',final2)

dilation3 = cv2.dilate(img_thresh13,kernel1,iterations = 1)
cv2.imwrite ('result\dilation3.png',dilation3)
erosion3 = cv2.erode(dilation3,kernel2,iterations = 1)
cv2.imwrite ('result\erosion3.png',erosion3)
final3 = cv2.dilate(erosion3,kernel3,iterations = 1)
cv2.imwrite ('result\saleh3.png',final3)


# in meanwhile run the tsseract and then importing the tesseract text file

sepid1 = open ("result\saleh1.txt", "r")
saleh1 = sepid1.read(5)
#print (saleh1.read(5))
#saleh1.close()

sepid2 = open ("result\saleh2.txt", "r")
saleh2 = sepid2.read(5)
#print (saleh2.read(5))
#saleh2.close()

sepid3 = open ("result\saleh3.txt", "r")
saleh3 = sepid3.read(5)

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


if saleh3 == "EITTE":
    print("BITTE WÄHLEN")

elif saleh3 == "GERIT":
    print("GERÄT HEIZT AUF")

elif saleh3 == "PFLIO":
    print("PFLEGE DRÜCKEN)")

else:
    print("please try again")



#from tesseract import image_to_string

#print image_to_string(Image.open('test.png'))
#print image_to_string(Image.open('test-english.jpg'), lang='eng')



#usrimg = Image.open('img_thresh.png')
## Saving the image as tesseract can read.
#captcha.save('temp.bmp', dpi=(200,200))
## Invoking tesseract from python to extract characters
#commands.getoutput('tesseract temp.bmp data')
## Reading the output generated in data.txt
##with open('data.txt', 'r') as data:
#    print data.readline().strip()

    
#print(pytesseract.image_to_string(Image.open('test.png')))
#print(pytesseract.image_to_string(Image.open('test-european.jpg'),lang='fra'))
 