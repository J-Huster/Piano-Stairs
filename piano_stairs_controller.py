import RPi.GPIO as GPIO
import time
import piano_stairs_model as model
import playsound
import pygobject

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 21
ECHO = 12

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, False)
GPIO.setup(ECHO, GPIO.IN)
time.sleep(2)

try:
    while True:
        # sensor one
        sensorNum = 1
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

        distance = model.getDistance(pulse_start, pulse_end)
        trigger = model.isTriggered(distance)
        #sound = model.getSound(sensorNum)
        playsound('/home/johaha/Desktop/test_sound.py')
        
except:
    GPIO.cleanup()
