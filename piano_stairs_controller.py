import RPi.GPIO as GPIO
import time
import piano_stairs_model as model
import pygame
pygame.mixer.init()

#import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set up sensor number variables
trig1 = 4  # sends a pulse to iniate measurement
echo1 = 17  # measures the time for pulse to return after pucing off the closest object

trig2 = 27
echo2 = 22

trig3 = 19
echo3 = 26

trig4 = 18
echo4 = 23

trig5 = 25
echo5 = 24

trig6 = 16
echo6 = 20

sensors = [trig1, echo1, trig2, echo2, trig3, echo3, trig4, echo4, trig5, echo5, trig6, echo6]

# for loop sets up all of the sensors (doesn't work)
for s in sensors:
    if sensors.index(s) % 2 == 0:
        TRIG = sensors[sensors.index(s)]
        GPIO.setup(TRIG, GPIO.OUT)  # sets up trig sensor as output
        GPIO.output(TRIG, False)  # sets output to be false
    if sensors.index(s) % 2 != 0:
        ECHO = sensors[sensors.index(s)]
        GPIO.setup(ECHO, GPIO.IN)  # sets up echo sensor as input
    time.sleep(.01)  # pauses program for .01 second

try:
    while True:
        for n in range(0, len(sensors), 2):
            TRIG = sensors[n]
            # send out pulse signal
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            
            n += 1
            ECHO = sensors[n]
            # will record last time echo is low
            while GPIO.input(ECHO) == 0:
                pulse_start = time.time()

            # will record last time echo is high
            while GPIO.input(ECHO) == 1:
                pulse_end = time.time()       

            distance = model.getDistance(pulse_start, pulse_end)
            print(distance)
            trigger = model.isTriggered(distance)
            sound = model.getSound(n)
            
            if trigger:
                model.playSound(sound)
except:
    GPIO.cleanup()