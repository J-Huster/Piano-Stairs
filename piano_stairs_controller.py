import RPi.GPIO as GPIO
import time
import piano_stairs_model as model

import pygame
pygame.mixer.init()

#import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 21
ECHO = 12

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, False)
GPIO.setup(ECHO, GPIO.IN)
time.sleep(2)

#try:
while True:
    # sensor one
    sensorNum = 1
    # send out pulse signal
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # will record last time echo is low
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    # will record last time echo is high
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()       

    distance = model.getDistance(pulse_start, pulse_end)
    print(distance)
    trigger = model.isTriggered(distance) 
    sound = model.getSound(1)
        
    
    #pygame.mixer.music.load("test_sound.mp3")
    #pygame.mixer.music.play()
    #time.sleep(2)
    if trigger:
        model.playSound()

#except:
    #GPIO.cleanup()
