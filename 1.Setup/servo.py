import RPi.GPIO as GPIO
import time
 
pin = 40 # PWM pin num 18
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 300)
p.start(0)
cnt = 0
try:
    while True:
        p.ChangeDutyCycle(25)
        print "angle : 1"
        time.sleep(1)
        p.ChangeDutyCycle(50)
        print "angle : 5"
        time.sleep(1)
        p.ChangeDutyCycle(75)
        print "angle : 8"
        time.sleep(1)
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()

