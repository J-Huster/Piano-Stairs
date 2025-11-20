import time
import pygame
pygame.mixer.init()

def getDistance(start, end):
    duration = end - start
    distance = 17150 * (duration / 2)
    return distance

def isTriggered(x):
    if x < 10:
        return True
    return False

def getSound(num):
    if num == 1:
        return "/home/johaha/Desktop/Piano-Stairs/test_sound.mp3"
    elif num == 3:
        return "/home/johaha/Desktop/Piano-Stairs/test_sound_2.mp3"
    else:
        return None

def playSound(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
    time.sleep(1)
