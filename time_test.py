import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)

base = False
count = 0
while True:
    try:
        input = GPIO.input(20)
        print (GPIO.input(20))
        if (input == True and base == False):
            base = not base
            start_time = time.time()
            elapsed_time1 = time.time() - start_time
            print (elapsed_time1)
        elif (input == False and base == True):
            base = not base
            elapsed_time2 = time.time() - start_time
            print (elapsed_time2)
            if (elapsed_time2 < 0.5 and (count <= 2)):
                count = count +1
            else:
                count = 0
            print (count)
        else:
            base = base
    except KeyboardInterrupt:
        GPIO.cleanup()
