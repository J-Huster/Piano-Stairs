def getSound():
    return "sound"

def getDistance(start, end):
    duration = end - start
    distance = 17150 * (duration / 2)
    return distance

def isTriggered(x):
    if x < 300:
        return True
    return False

def getSound(num):
    if num == 1:
        return "sond.mp3"
    else:
        return None
