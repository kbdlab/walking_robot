# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 20:57:43 2019

@author: SHF_W
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 03:19:52 2019

@author: kbdlab2

motor
Camera Calibrated
select white
keyboard control (PWM)
decision

"""
import cv2
import numpy as np
import time
import math
import glob
import os
import image_process as img

def select_white(image, white):
    lower = np.uint8([white,white,white])
    upper = np.uint8([255,255,255])
    white_mask = cv2.inRange(image, lower, upper)
    return white_mask
    
def first_nonzero(arr, axis, invalid_val=-1):
    arr = np.flipud(arr)
    mask = arr!=0
    return np.where(mask.any(axis=axis), mask.argmax(axis=axis), invalid_val)
    
def set_path1(image, upper_limit, fixed_center = 'False', sample=10):
    height, width = image.shape
    height = height-1
    width = width-1
    center=int(width/2)
    left=0
    right=width
    white_distance = np.zeros(width)
       
    if not fixed_center: 
        for i in range(center):
            if image[height,center-i] > 200:
                left = center-i
                break            
        for i in range(center):
            if image[height,center+i] > 200:
                right = center+i
                break    
        center = int((left+right)/2)      

    for i in range(left,right,sample):
        for j in range(upper_limit):
            if image[height-j,i] > 200:                
                white_distance[i]=j
                break
    
    left_sum = np.sum(white_distance[left:center])
    right_sum = np.sum(white_distance[center:right])
    forward_sum = np.sum(white_distance[center-10:center+10])
    
    if forward_sum > 2000:
        result = 'forward'
    elif left_sum > right_sum + 500:
        result = 'left'
    elif left_sum < right_sum - 500:
        result = 'right'
    else:
        result = 'forward'
    
    return result, left_sum, right_sum
         
def set_path2(image, upper_limit, fixed_center = 'False'):
    height, width = image.shape
    image = image[height-upper_limit:,:]
    height = upper_limit-1
    width = width-1
    center=int(width/2)
    left=0
    right=width       
    
    if not fixed_center:
        center = int((left+right)/2)        
        if image[height][:center].min(axis=0) == 255:
            left = 0
        else:
            left = image[height][:center].argmin(axis=0)
        
        if image[height][center:].max(axis=0) == 0:
            right = width
        else:    
            right = center+image[height][center:].argmax(axis=0)        
        center = int((left+right)/2)  
    
    image = np.flipud(image) # in python3, np.flip(image, axis=0)
    mask = image!= 0
    integral = np.where(mask.any(axis=0), mask.argmax(axis=0), height) 
    
    left_sum = np.sum(integral[left:center])
    right_sum = np.sum(integral[center:right])
    forward_sum = np.sum(integral[center-10:center+10])   
    
    if forward_sum > 2000:
        result = 'forward'
    elif left_sum > right_sum + 500:
        result = 'left'
    elif left_sum < right_sum - 500:
        result = 'right'
    else:
        result = 'forward'
    
    return result, left_sum, right_sum
    
    
def set_path3(image, forward_criteria):
    height, width = image.shape
    height = height-1
    width = width-1
    center=int(width/2)
    left=0
    right=width
    
    center = int((left+right)/2)        
    
    try:
        '''if image[height][:center].min(axis=0) == 255:
            left = 0
        else:
            left = image[height][:center].argmin(axis=0)    
        if image[height][center:].max(axis=0) == 0:
            right = width
        else:    
            right = center+image[height][center:].argmax(axis=0)  
            q
        center = int((left+right)/2)'''  
        
        print(int(first_nonzero(image[:,center],0,height)))
        forward = min(int(height),int(first_nonzero(image[:,center],0,height))-1)
        #print(height, first_nonzero(image[:,center],0,height))
        
        left_line = first_nonzero(image[height-forward:height,center:],1, width-center)
        right_line = first_nonzero(np.fliplr(image[height-forward:height,:center]),1, center)
        
        center_y = (np.ones(forward)*2*center-left_line+right_line)/2-center
        center_x = np.vstack((np.arange(forward), np.zeros(forward)))
        m, c = np.linalg.lstsq(center_x.T, center_y, rcond=-1)[0]
        if forward < 20 or forward < 50 and abs(m) < 0.35:
            result = 'backward'
        elif abs(m) < forward_criteria:
            result = 'forward'
        elif m > 0:
            result = 'left'
        else:
            result = 'right'
    except:
        result = 'backward'
        m = 0
    
    return result, round(m,4), forward


if __name__ == "__main__":
    start_time=time.time()
    path = './raw_image_set_1/*.png'
    file_list = glob.glob(path)
    cnt = 0
    for i in file_list:
        image = cv2.imread(i)
        name, extension = os.path.splitext(os.path.basename(i))
        masked_image=select_white(image,160)
        cv2.imshow("video", masked_image)
        result=set_path3(masked_image,0.25)
        #result=set_path1(masked_image,120)
        if result[0][0] in name[-3:]:
            answer = '○'
            cnt += 1
        else:
            answer = '×'
        cv2.waitKey(0)
        print(name, answer, result)
    cv2.destroyAllWindows()
    print('\nAvearage FPS:', round(len(file_list)/(time.time()-start_time),2), "Acurracy:", str(round(100*cnt/len(file_list), 2))+" %")