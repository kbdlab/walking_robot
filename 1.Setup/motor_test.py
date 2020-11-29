import time
import RPi.GPIO as GPIO

# pin definition
motor1A = 16
motor1B = 18

# pin setting
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1A,GPIO.OUT)
GPIO.setup(motor1B,GPIO.OUT)

# pin output setting
GPIO.output(motor1A, GPIO.HIGH) # GPIO.HIGH == 1
GPIO.output(motor1B, GPIO.LOW)  # GPIO.LOW  == 0
time.sleep(5)

# reverse
GPIO.output(motor1A, GPIO.LOW)
GPIO.output(motor1B, GPIO.HIGH)
time.sleep(5)

# GPIO setting reset
GPIO.cleanup()

