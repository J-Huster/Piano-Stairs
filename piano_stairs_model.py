import time
import pygame
pygame.mixer.init()

def getSound():
    return "sound"

def getDistance(start, end):
    duration = end - start
    distance = 17150 * (duration / 2)
    return distance

def isTriggered(x):
    if x < 50:
        return True
    return False

def getSound(num):
    if num == 1:
        return "/home/johaha/Desktop/Piano-Stairs/test_sound.mp3"
    else:
        return None

def playSound():
    pygame.mixer.music.load("test_sound.mp3")
    pygame.mixer.music.play()
    time.sleep(2)
