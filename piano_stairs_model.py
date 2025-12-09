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
        return "/home/johaha/Piano-Stairs/key_1.mp3"
    elif num == 3:
        return "/home/johaha/Piano-Stairs/key_2.mp3"
    elif num == 5:
        return "/home/johaha/Piano-Stairs/key_3.mp3"
    elif num == 7:
        return "/home/johaha/Piano-Stairs/key_4.mp3"
    elif num == 9:
        return "/home/johaha/Piano-Stairs/key_5.mp3"
    elif num == 11:
        return "/home/johaha/Piano-Stairs/key_6.mp3"
    elif num == 13:
        return "/home/johaha/Piano-Stairs/key_7.mp3"
    elif num == 15:
        return "/home/johaha/Piano-Stairs/key_8.mp3"
    else:
        return None

def playSound(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
    time.sleep(1)
