import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 21
ECHO = 12

GPIO.setup(TRIG, GPIO.OUT, False)
GPIO.setup(ECHO, GPIO.IN)
time.sleep(2)

try:
    while True:
        # send out pulse signal
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        # will record last time echo is low
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        # will record last time echo is high
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()       

        pulse_duration = pulse_end - pulse_start
        distance = 17150 * (pulse_duration / 2)
        print(f"{distance} cm")
except:
    GPIO.cleanup()