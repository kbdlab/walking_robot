#import gpio_dummy as GPIO
import gpio_dummy
GPIO = gpio_dummy.GPIO()

import numpy as np

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
