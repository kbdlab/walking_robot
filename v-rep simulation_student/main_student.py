# -*- coding: utf-8 -*-
"""
@author: KBDLAB
"""

# in raspberry pi, use import RPi.GPIO as GPIO
import gpio_dummy
GPIO = gpio_dummy.GPIO()
##############################################

import time
import cv2
import numpy as np
import linecache
import sys

motor1A = 11
motor1B = 13
motor2A = 16
motor2B = 18
echo = 26

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1A, GPIO.OUT)
GPIO.setup(motor1B, GPIO.OUT)
GPIO.setup(motor2A, GPIO.OUT)
GPIO.setup(motor2B, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

p1A = GPIO.PWM(motor1A, 600)
p1B = GPIO.PWM(motor1B, 600)
p2A = GPIO.PWM(motor2A, 600)
p2B = GPIO.PWM(motor2B, 600)
p1A.start(100)
p1B.start(100)
p2A.start(100)
p2B.start(100)    

def motor(left, right):
    left = np.clip(left, -100 , 100)
    right = np.clip(right, -100, 100)
    
    if left > 0:
        left_f = left
        left_b = 0
    else:
        left_f = 0
        left_b = -left
    	
    if right > 0:
        right_f = right
        right_b = 0
    else:
        right_f = 0
        right_b = -right
        
    p1A.ChangeDutyCycle(left_f)
    p1B.ChangeDutyCycle(left_b)
    p2A.ChangeDutyCycle(right_f)
    p2B.ChangeDutyCycle(right_b)  

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print ('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))

def us():
    return GPIO.input(echo)
    
def driver():
    path = './datafile/vision.png'  
    
    # This 2 line detect v-rep simulation's status.
    # GPIO no. 39 is ground pin. it need to be edited in real raspberry pi code.
    GPIO.setup(39, GPIO.IN)
    while GPIO.input(39) == 0:
        try:
            # get image - edit it raspberry pi.
            image = cv2.imread(path)
            if image is None:
                continue # image read error exceptions    
            
            left = 100 * (int(time.time()) % 100) / 100
            right = 100 * (int(time.time()) % 100) / 100   
            
            motor(left, right)
           
            cv2.imshow('Image', image)
            key = cv2.waitKey(1) & 0xFF       
        except:
            PrintException()
            motor(0,0)
           
        time.sleep(0.02)   
        
        if key == ord('q'):  
            break
    cv2.destroyAllWindows()
        
if __name__ == '__main__':        
    print('Start')
    driver()    
    
    GPIO.cleanup()