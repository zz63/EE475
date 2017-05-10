import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)
GPIO.setup(4, GPIO.OUT)
camera = PiCamera()


#input = GPIO.input(38)
#GPIO.setup(4, GPIO.OUT,initial=GPIO.HIGH)

#GPIO.output(4, GPIO.input(20))
'''count = 0
try:
    camera.start_preview()
    while (1):
        count += 1
        input = GPIO.input(20)
        sleep(5)
        if (input == True):
            GPIO.output(4, GPIO.HIGH)
            camera.capture('home/pi/Desktop/image%s.jpg' % count)
            print '1'
        else:
            GPIO.output(4, GPIO.LOW)
            print '0'
    camera.stop_preview()

except KeyboardInterrupt:
    GPIO.cleanup()
'''
camera.start_preview(alpha = 200)
count = 0
while True:
    try:
        input = GPIO.input(20)
        sleep(0.5)
        if (input == True):
            count += 1
            GPIO.output(4,GPIO.HIGH)
            camera.capture('/home/pi/Desktop/image%s.jpg' % count)
            print '1'
        else:
            GPIO.output(4, GPIO.LOW)
            print '0'
    except KeyboardInterrupt:
        camera.stop_preview()
        GPIO.cleanup()
