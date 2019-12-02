import time
import RPi.GPIO as GPIO

motor1A = 16
motor1B = 18
motor2A = 15
motor2B = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor1A,GPIO.OUT)
GPIO.setup(motor1B,GPIO.OUT)
GPIO.setup(motor2A,GPIO.OUT)
GPIO.setup(motor2B,GPIO.OUT)

p1A = GPIO.PWM(motor1A, 1000)
p1B = GPIO.PWM(motor1B, 1000)
p2A = GPIO.PWM(motor2A, 1000)
p2B = GPIO.PWM(motor2B, 1000)
p1A.start(0)
p1B.start(0)
p2A.start(0)
p2B.start(0)    

p1A.ChangeDutyCycle(100)
p1B.ChangeDutyCycle(0)
p2A.ChangeDutyCycle(100)
p2B.ChangeDutyCycle(0)
time.sleep(3)
p1A.ChangeDutyCycle(0)
p1B.ChangeDutyCycle(80)
p2A.ChangeDutyCycle(0)
p2B.ChangeDutyCycle(100)
time.sleep(3)
p1A.ChangeDutyCycle(70)
p1B.ChangeDutyCycle(0)
p2A.ChangeDutyCycle(0)
p2B.ChangeDutyCycle(100)
time.sleep(3)
p1A.ChangeDutyCycle(0)
p1B.ChangeDutyCycle(100)
p2A.ChangeDutyCycle(60)
p2B.ChangeDutyCycle(0)
time.sleep(3)

p2A.ChangeDutyCycle(0)
p2B.ChangeDutyCycle(0)
for i in range(101):
    p1A.ChangeDutyCycle(i)
    p1B.ChangeDutyCycle(0)
    print(i)
    time.sleep(0.2)

GPIO.cleanup()


