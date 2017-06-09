# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 12:55:19 2017

@author: Saleh Firoozabadi
"""

from im_processing import im_processing
from LSQ import LSQ


img = cv2.imread ("import\d1.jpg")


recognizedtext = LSQ (img)
print (recognizedtext)