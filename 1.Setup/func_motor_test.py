import RPi.GPIO as GPIO
import numpy as np
import time
    
def motor(left, right):
	left = np.clip(left, -100 , 100)
	right = np.clip(right, -100, 100)
	print(left,right)

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
	print(left_f, left_b, right_f, right_b)
	time.sleep(0.00001)
	p1A.ChangeDutyCycle(left_f)
	p1B.ChangeDutyCycle(left_b)
	p2A.ChangeDutyCycle(right_f)
	p2B.ChangeDutyCycle(right_b)

# gpio pin setting
motor1A = 16
motor1B = 18
motor2A = 15
motor2B = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1A,GPIO.OUT)
GPIO.setup(motor1B,GPIO.OUT)
GPIO.setup(motor2A,GPIO.OUT)
GPIO.setup(motor2B,GPIO.OUT)
p1A = GPIO.PWM(motor1A, 500)
p1B = GPIO.PWM(motor1B, 500)
p2A = GPIO.PWM(motor2A, 500)
p2B = GPIO.PWM(motor2B, 500)
p1A.start(0)
p1B.start(0)
p2A.start(0)
p2B.start(0)


motor(100,100)
time.sleep(50)
motor(100, 0)
time.sleep(5)
motor(-100, 0)
time.sleep(5)
motor(0,-100)
time.sleep(5)
