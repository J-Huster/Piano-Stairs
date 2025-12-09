import RPi.GPIO as GPIO
import time
import piano_stairs_model as model
import pygame
pygame.mixer.init()

# setup GPIO board
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# setup sensor number variables
# trig sends a pulse to iniate measurement
# echo measures the time for pulse to return after pucing off the closest object

# sensor 1 
trig1 = 4 
echo1 = 17

# sensor 2
trig2 = 27
echo2 = 22

# sensor 3
trig3 = 19
echo3 = 26

# sensor 4
trig4 = 18
echo4 = 23

# sensor 5
trig5 = 25
echo5 = 24

# sensor 6
trig6 = 16
echo6 = 20

# setup loop containing varaiables for the trig and echo components of the sensors
sensors = [trig1, echo1, trig2, echo2, trig3, echo3, trig4, echo4, trig5, echo5, trig6, echo6]

# for loop sets up all of the sensors
for s in sensors:
    if sensors.index(s) % 2 == 0:
        TRIG = sensors[sensors.index(s)]
        GPIO.setup(TRIG, GPIO.OUT)  # sets up trig sensor as output
        GPIO.output(TRIG, False)  # sets output to be false
    if sensors.index(s) % 2 != 0:
        ECHO = sensors[sensors.index(s)]
        GPIO.setup(ECHO, GPIO.IN)  # sets up echo sensor as input
    time.sleep(.01)  # pauses program for .01 second

# run infinite loop unless an exception occurs, then turn off power to GPIO pins
try:
    while True:
        # loop through all of the sensors
        for n in range(0, len(sensors), 2):
            TRIG = sensors[n]  # get number for trig sensor
            # send out pulse signal
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)

            # increment loop variable by one to access variable after trig, echo
            n += 1
            ECHO = sensors[n]  # get number for echo sensor
            
            # will record last time echo is low
            while GPIO.input(ECHO) == 0:
                pulse_start = time.time()

            # will record last time echo is high
            while GPIO.input(ECHO) == 1:
                pulse_end = time.time()       

            # calculate the distance between sensor and nearest object
            distance = model.getDistance(pulse_start, pulse_end)
            print(distance)
            # return if distance is less than a certain number (ex. distance to wall)
            trigger = model.isTriggered(distance)
            # get sound assigned to certain sensor
            sound = model.getSound(n)

            #test if nearest object is closer than certain distance 
            if trigger:
                model.playSound(sound)  # play sound through speaker
except:
    GPIO.cleanup()  # turn off all power to GPIO pins
