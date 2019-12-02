# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:12:13 2019

border

@author: SHF_W
"""

import cv2
import glob
import os
from datetime import datetime
       
path = './files/*.png'
#createFolder('./data_'+timestamp)
file_list = glob.glob(path)
for item in file_list:
    image = cv2.imread(item)
    h, l, c = image.shape   

    processed = cv2.copyMakeBorder(image,25,25,25,25,cv2.BORDER_CONSTANT,value=[255,255,255])
    name = './'+'files2'+'/'+os.path.basename(item)
    print(name)
    cv2.imshow('v',processed)
    cv2.waitKey(1000)
                                               
    cv2.imwrite(name, processed)
    
cv2.destroyAllWindows()
    
    

	



