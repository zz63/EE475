import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from gpiozero import Button

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)
left_button = Button(17)
right_button = Button(4)
camera = PiCamera()

base = True
count = 0
picture = 0
#left_button.wait_for_press()
camera.start_preview(alpha = 200)
while True:
    try:
        input = GPIO.input(20)
        if (input == False and base == True):
            base = not base
            start_time = time.time()
            #elapsed_time1 = time.time() - start_time
            #print (elapsed_time1)
        elif (input == True and base == False):
            base = not base
            elapsed_time2 = time.time() - start_time
            print (elapsed_time2)
            if (elapsed_time2 < 0.5):
                if (count < 4):
                    count = count +1
                else:
                    count = 0
            else:
                count = 0
            print (count)
            if (count == 3):
                picture = picture +1
                camera.capture('/home/pi/Desktop/image%s.jpg' % picture)
            else:
                print ('try again!')
        else:
            base = base
    except KeyboardInterrupt:
    #except right_button.wait_for_press():
        camera.stop_preview()
        GPIO.cleanup()
        exit
