import RPi.GPIO as GPIO
import time
import piano_stairs_model as model
import pygame
pygame.mixer.init()

#import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set up sensor number variables
trig1 = 17  # sends a pulse to iniate measurement
echo1 = 4  # measures the time for pulse to return after pucing off the closest object

GPIO.setup(trig1, GPIO.OUT)  # sets up trig sensor as output
GPIO.output(trig1, False)  # sets output to be false
GPIO.setup(echo1, GPIO.IN)  # sets up echo sensor as input
time.sleep(.01)  # pauses program for .01 second

trig2 = 22
echo2 = 27

GPIO.setup(trig2, GPIO.OUT)  # sets up trig sensor as output
GPIO.output(trig2, False)  # sets output to be false
GPIO.setup(echo2, GPIO.IN)  # sets up echo sensor as input
time.sleep(.01)  # pauses program for .01 second

trig3 = 6
echo3 = 5

GPIO.setup(trig3, GPIO.OUT)  # sets up trig sensor as output
GPIO.output(trig3, False)  # sets output to be false
GPIO.setup(echo3, GPIO.IN)  # sets up echo sensor as inputtime.sleep(.01)  # pauses program for .01 second
time.sleep(.01)  # pauses program for .01 second

trig4 = 1
echo4 = 1

#GPIO.setup(trig4, GPIO.OUT)  # sets up trig sensor as output
#GPIO.output(trig4, False)  # sets output to be false
#GPIO.setup(echo4, GPIO.IN)  # sets up echo sensor as input
#time.sleep(.01)  # pauses program for .01 second

trig5 = 1
echo5 = 1

#GPIO.setup(trig5, GPIO.OUT)  # sets up trig sensor as output
#GPIO.output(trig5, False)  # sets output to be false
#GPIO.setup(echo5, GPIO.IN)  # sets up echo sensor as input
#time.sleep(.01)  # pauses program for .01 second

trig6 = 1
echo6 = 1

#GPIO.setup(trig6, GPIO.OUT)  # sets up trig sensor as output
#GPIO.output(trig6, False)  # sets output to be false
#GPIO.setup(echo6, GPIO.IN)  # sets up echo sensor as input
#time.sleep(.01)  # pauses program for .01 second

trig7 = 1
echo7 = 1

#GPIO.setup(trig7, GPIO.OUT)  # sets up trig sensor as output
#GPIO.output(trig7, False)  # sets output to be false
#GPIO.setup(echo7, GPIO.IN)  # sets up echo sensor as input
#time.sleep(.01)  # pauses program for .01 second

trig8 = 1
echo8 = 1

#GPIO.setup(trig8, GPIO.OUT)  # sets up trig sensor as output
#GPIO.output(trig8, False)  # sets output to be false
#GPIO.setup(echo8, GPIO.IN)  # sets up echo sensor as input
#time.sleep(.01)  # pauses program for .01 second

sensors = [trig1, echo1, trig2, echo2, trig3, echo3] #, trig4, echo4, trig5, echo5, trig6, echo6, trig7, echo7, trig8, echo8]

# for loop sets up all of the sensors (doesn't work)
#for s in range(len(sensors)):
#    if s % 2 == 0:
#        TRIG = sensors[s]
#        GPIO.setup(TRIG, GPIO.OUT)  # sets up trig sensor as output
#        GPIO.output(TRIG, False)  # sets output to be false
#    if s % 2 != 0:
#        ECHO = sensors[s]
#        GPIO.setup(ECHO, GPIO.IN)  # sets up echo sensor as input
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
