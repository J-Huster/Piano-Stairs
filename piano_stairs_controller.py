import RPi.GPIO as GPIO
import time
import piano_stairs_model as model
import pygame
pygame.mixer.init()

#import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set up sensor number variables
trig1 = 21  # sends a pulse to iniate measurement
echo1 = 12  # measures the time for pulse to return after pucing off the closest object

GPIO.setup(trig1, GPIO.OUT)  # sets up trig sensor as output
GPIO.output(trig1, False)  # sets output to be false
GPIO.setup(echo1, GPIO.IN)  # sets up echo sensor as input
time.sleep(.01)  # pauses program for .01 second

trig2 = 16
echo2 = 20

GPIO.setup(trig2, GPIO.OUT)  # sets up trig sensor as output
GPIO.output(trig2, False)  # sets output to be false
GPIO.setup(echo2, GPIO.IN)  # sets up echo sensor as input
time.sleep(.01)  # pauses program for .01 second

trig3 = 1
echo3 = 1

trig4 = 1
echo4 = 1

trig5 = 1
echo5 = 1

trig6 = 1
echo6 = 1

trig7 = 1
echo7 = 1

trig8 = 1
echo8 = 1

sensors = [trig1, echo1, trig2, echo2]

# sets up all of the sensors
#for s in range(len(sensors)):
#    if s % 2 == 0:
#        GPIO.setup(s, GPIO.OUT)  # sets up trig sensor as output
#        GPIO.output(s, False)  # sets output to be false
#    if s % 2 != 0:
#        GPIO.setup(s, GPIO.IN)  # sets up echo sensor as input
#    time.sleep(.01)  # pauses program for .01 second

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
