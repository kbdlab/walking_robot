# -*- coding: utf-8 -*-
"""
@author: KBDLAB
"""

import os
import cv2
import numpy as np
import itertools as it, glob

def multiple_file_types(*patterns):
    return it.chain.from_iterable(glob.iglob(pattern) for pattern in patterns)

def default_put_text(_str, pos):
    cv2.putText(out, _str, pos, font, 1, (255, 255, 255), 1)

types = ('*.png', '*.jpg')
images = []
font = cv2.FONT_HERSHEY_DUPLEX
for image_path in multiple_file_types('./sample/*.jpg', './sample/*.png'):
    image_array = cv2.imread(image_path)
    h,l,c = image_array.shape
    
    if h > 480:
        image_array = cv2.resize(image_array, None, fx = 300/h, fy = 300/h, interpolation=cv2.INTER_CUBIC)
        h, l, c = image_array.shape
    
    image_array_gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
    image_array_edge = cv2.Canny(cv2.GaussianBlur(image_array_gray, (5,5),0), 100, 200)
    
    out_u = np.hstack((np.zeros([h,l,c], dtype='uint8'),image_array))
    out_l = cv2.cvtColor(np.hstack((image_array_gray, image_array_edge)), cv2.COLOR_GRAY2BGR)  
    out = np.vstack((out_u, out_l))
    
    default_put_text(os.path.basename(image_path), (10,25))
    default_put_text(str((h, l, c)), (10, 60))
    
    cv2.imshow('image', out)
    cv2.waitKey(0)
cv2.destroyAllWindows()
    
    

