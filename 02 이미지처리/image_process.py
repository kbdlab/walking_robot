import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import os
import glob

def show_BGR(image, axis='off', interpolation='None'):
    result = image[:,:,::-1]
    plt.axis(axis)
    plt.imshow(result, interpolation=interpolation)
    
def make_black(image, threshold = 100):
    height, length, channel = image.shape 
    for h in range(height):
        for l in range(length):
            flag = True
            for c in range(channel):
                flag *= image[h,l,c] < threshold
            if flag:
                image[h,l] = np.zeros(3, dtype='uint8')
    return image

def show_BGR2(image, axis='off'):
    result = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.axis(axis)
    plt.imshow(result, interpolation='bicubic')
    
def make_black2(image, threshold = 100):
    height, length, channel = image.shape 
    lower_bound = np.ones(channel)*threshold
    upper_bound = np.ones(channel)*255
    return cv2.inRange(image, lower_bound, upper_bound)
                       
def select_color(image, lower, upper):   
    image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)   
    return cv2.inRange(image_HSV, lower, upper)

def edge_detection(image, thres=(100,200), blur=True):
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if blur:
        image = cv2.GaussianBlur(image, (5,5),0)
    return cv2.Canny(image, thres[0], thres[1])

def hough_transform(image, edges):
    lines = cv2.HoughLines(edges,1,np.pi/180,200)
    try:
        for line in lines:        
            rho,theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)
            print('rho', rho, ' | theta', theta)
    except:
        pass
    return image

def region_of_interest(image, w=0.05, point=(0.2,0.5)):
    height, width = image.shape
        
    point1 = ( int(width*w), height )
    point2 = ( int(width*(1-w)), height )
    point3 = ( int(width*(1-point[0])), int(height*point[1]) )            
    point4 = ( int(width*point[0]), int(height*point[1]) ) 
    
    poly = np.array([point1, point2, point3, point4])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, [poly], 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


if __name__ == '__main__':
    image_array = cv2.imread('./image/sample_image.jpg')
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    