import RPi.GPIO as GPIO
from subprocess import call
import time

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Tree no 19

GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW) # Star
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW) # Tree no 1 Red
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) # Tree no 7 Red
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW) # Tree no 16 Green
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) # Tree no 22 Red
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Tree no 6 Blue
GPIO.setup(9, GPIO.OUT, initial=GPIO.LOW) # Tree no 14 Green
GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW) # Tree no 8 Blue
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) # Tree no 21 Blue
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # Tree no 15 Green
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) # Tree no 3 Red
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW) # Tree no 2 Green
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # Tree no 9 Blue
GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) # Tree no 10 Green
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # Tree no 20 Red
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW) # Tree no 18 Red
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) # Tree no 17 Red
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) # Tree no 24 Red
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW) # Tree no 23 Green
GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW) # Tree no 13 Red
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW) # Tree no 5 Blue
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # Tree no 12 Red
GPIO.setup(27, GPIO.OUT, initial=GPIO.LOW) # Tree no 11 Blue

buttonStatus = 0

def buttonStateChanged(pin):

    global buttonStatus

    if not (GPIO.input(pin)):
        
        buttonStatus = buttonStatus + 1

        if (buttonStatus == 7):
            buttonStatus = 0

GPIO.add_event_detect(14, GPIO.BOTH, callback=buttonStateChanged,bouncetime=400)


def allOff():
    GPIO.output(2, False) # Star
    GPIO.output(4, False) # Tree no 1 Red
    GPIO.output(5, False) # Tree no 7 Red
    GPIO.output(6, False) # Tree no 16 Green
    GPIO.output(7, False) # Tree no 22 Red
    GPIO.output(8, False) # Tree no 6 Blue
    GPIO.output(9, False) # Tree no 14 Green
    GPIO.output(10, False) # Tree no 8 Blue
    GPIO.output(11, False) # Tree no 21 Blue
    GPIO.output(12, False) # Tree no 15 Green
    GPIO.output(13, False) # Tree no 3 Red
    GPIO.output(15, False) # Tree no 2 Green
    GPIO.output(16, False) # Tree no 9 Blue
    GPIO.output(17, False) # Tree no 10 Green
    GPIO.output(18, False) # Tree no 20 Red
    GPIO.output(19, False) # Tree no 18 Red
    GPIO.output(20, False) # Tree no 17 Red
    GPIO.output(22, False) # Tree no 24 Red
    GPIO.output(23, False) # Tree no 23 Green
    GPIO.output(24, False) # Tree no 13 Red
    GPIO.output(25, False) # Tree no 5 Blue
    GPIO.output(26, False) # Tree no 12 Red
    GPIO.output(27, False) # Tree no 11 Blue

def around():

    aroundSleep = 0.5
   
    allOff()
    GPIO.output(2, True) # Star
    GPIO.output(5, True) # Tree no 7 Red
    GPIO.output(11, True) # Tree no 21 Blue
    GPIO.output(12, True) # Tree no 15 Green
    GPIO.output(19, True) # Tree no 18 Red
    GPIO.output(26, True) # Tree no 12 Red
    time.sleep(aroundSleep)

    allOff()
    GPIO.output(2, True) # Star
    GPIO.output(8, True) # Tree no 6 Blue
    GPIO.output(6, True) # Tree no 16 Green
    GPIO.output(7, True) # Tree no 22 Red
    GPIO.output(27, True) # Tree no 11 Blue
    GPIO.output(18, True) # Tree no 20 Red
    GPIO.output(15, True) # Tree no 2 Green
    time.sleep(aroundSleep)

    allOff()
    GPIO.output(2, True) # Star
    GPIO.output(4, True) # Tree no 1 Red
    GPIO.output(17, True) # Tree no 10 Green
    GPIO.output(9, True) # Tree no 14 Green
    GPIO.output(22, True) # Tree no 24 Red
    GPIO.output(10, True) # Tree no 8 Blue
    time.sleep(aroundSleep)

    allOff()
    GPIO.output(2, True) # Star
    GPIO.output(23, True) # Tree no 23 Green
    GPIO.output(24, True) # Tree no 13 Red
    GPIO.output(25, True) # Tree no 5 Blue
    GPIO.output(13, True) # Tree no 3 Red
    GPIO.output(16, True) # Tree no 9 Blue
    GPIO.output(20, True) # Tree no 17 Red
    time.sleep(aroundSleep)

def allOn():

    GPIO.output(2, True) # Star
    GPIO.output(4, True) # Tree no 1 Red
    GPIO.output(5, True) # Tree no 7 Red
    GPIO.output(6, True) # Tree no 16 Green
    GPIO.output(7, True) # Tree no 22 Red
    GPIO.output(8, True) # Tree no 6 Blue
    GPIO.output(9, True) # Tree no 14 Green
    GPIO.output(10, True) # Tree no 8 Blue
    GPIO.output(11, True) # Tree no 21 Blue
    GPIO.output(12, True) # Tree no 15 Green
    GPIO.output(13, True) # Tree no 3 Red
    GPIO.output(15, True) # Tree no 2 Green
    GPIO.output(16, True) # Tree no 9 Blue
    GPIO.output(17, True) # Tree no 10 Green
    GPIO.output(18, True) # Tree no 20 Red
    GPIO.output(19, True) # Tree no 18 Red
    GPIO.output(20, True) # Tree no 17 Red
    GPIO.output(22, True) # Tree no 24 Red
    GPIO.output(23, True) # Tree no 23 Green
    GPIO.output(24, True) # Tree no 13 Red
    GPIO.output(25, True) # Tree no 5 Blue
    GPIO.output(26, True) # Tree no 12 Red
    GPIO.output(27, True) # Tree no 11 Blue

while True:

# Just off mode
    if (buttonStatus == 0):
        allOff()

# Just on mode
    if (buttonStatus == 1):
        allOn()

# Quarter mode
    if (buttonStatus == 2):
        around()

# RGB mode
    if (buttonStatus == 3):
        RGBtime = 0.5

        allOff()
        GPIO.output(2, True) # Star
        GPIO.output(8, True) # Tree no 6 Blue
        GPIO.output(27, True) # Tree no 11 Blue
        GPIO.output(10, True) # Tree no 8 Blue
        GPIO.output(25, True) # Tree no 5 Blue
        GPIO.output(16, True) # Tree no 9 Blue
        GPIO.output(11, True) # Tree no 21 Blue
        time.sleep(RGBtime)

        allOff()
        GPIO.output(2, True) # Star
        GPIO.output(6, True) # Tree no 16 Green
        GPIO.output(12, True) # Tree no 15 Green
        GPIO.output(15, True) # Tree no 2 Green
        GPIO.output(17, True) # Tree no 10 Green
        GPIO.output(9, True) # Tree no 14 Green
        GPIO.output(23, True) # Tree no 23 Green
        time.sleep(RGBtime)

        allOff()
        GPIO.output(2, True) # Star
        GPIO.output(5, True) # Tree no 7 Red
        GPIO.output(19, True) # Tree no 18 Red
        GPIO.output(26, True) # Tree no 12 Red
        GPIO.output(7, True) # Tree no 22 Red
        GPIO.output(18, True) # Tree no 20 Red
        GPIO.output(4, True) # Tree no 1 Red
        GPIO.output(22, True) # Tree no 24 Red
        GPIO.output(24, True) # Tree no 13 Red
        GPIO.output(13, True) # Tree no 3 Red
        GPIO.output(20, True) # Tree no 17 Red
        time.sleep(RGBtime)

# Twinkle mode
    if (buttonStatus == 4):

        twinkleTime = 0.5

        allOff()
        GPIO.output(2, True) # Star
        GPIO.output(4, True) # Tree no 1 Red
        GPIO.output(9, True) # Tree no 14 Green
        GPIO.output(10, True) # Tree no 8 Blue

        GPIO.output(24, True) # Tree no 13 Red
        GPIO.output(16, True) # Tree no 9 Blue
        GPIO.output(13, True) # Tree no 3 Red

        GPIO.output(26, True) # Tree no 12 Red
        GPIO.output(11, True) # Tree no 21 Blue

        GPIO.output(7, True) # Tree no 22 Red
        GPIO.output(8, True) # Tree no 6 Blue
        GPIO.output(15, True) # Tree no 2 Green
        time.sleep(twinkleTime)

        allOff()
        GPIO.output(2, True) # Star
        GPIO.output(17, True) # Tree no 10 Green
        GPIO.output(22, True) # Tree no 24 Red

        GPIO.output(25, True) # Tree no 5 Blue
        GPIO.output(20, True) # Tree no 17 Red
        GPIO.output(23, True) # Tree no 23 Green

        GPIO.output(19, True) # Tree no 18 Red
        GPIO.output(5, True) # Tree no 7 Red
        GPIO.output(12, True) # Tree no 15 Green

        GPIO.output(6, True) # Tree no 16 Green
        GPIO.output(18, True) # Tree no 20 Red
        GPIO.output(27, True) # Tree no 11 Blue
        time.sleep(twinkleTime)

# Chase mode
    if (buttonStatus == 5):
        chaseTime = 0.1
        allOff()
        GPIO.output(26, True) # Tree no 12 Red
        time.sleep(chaseTime)
        allOff()
        GPIO.output(19, True) # Tree no 18 Red
        time.sleep(chaseTime)
        allOff()
        GPIO.output(2, True) # Star
        time.sleep(chaseTime)
        allOff()
        GPIO.output(11, True) # Tree no 21 Blue
        time.sleep(chaseTime)
        allOff()
        GPIO.output(5, True) # Tree no 7 Red
        time.sleep(chaseTime)
        allOff()
        GPIO.output(12, True) # Tree no 15 Green
        time.sleep(chaseTime)
        allOff()
        GPIO.output(7, True) # Tree no 22 Red
        time.sleep(chaseTime)
        allOff()
        GPIO.output(6, True) # Tree no 16 Green
        time.sleep(chaseTime)
        allOff()
        GPIO.output(8, True) # Tree no 6 Blue
        time.sleep(chaseTime)
        allOff()
        GPIO.output(27, True) # Tree no 11 Blue
        time.sleep(chaseTime)
        allOff()
        GPIO.output(18, True) # Tree no 20 Red
        time.sleep(chaseTime)
        allOff()
        GPIO.output(15, True) # Tree no 2 Green
        time.sleep(chaseTime)
        allOff()
        GPIO.output(4, True) # Tree no 1 Red
        time.sleep(chaseTime)
        allOff()
        GPIO.output(17, True) # Tree no 10 Green
        time.sleep(chaseTime)
        allOff()
        GPIO.output(9, True) # Tree no 14 Green
        time.sleep(chaseTime)
        allOff()
        GPIO.output(22, True) # Tree no 24 Red
        time.sleep(chaseTime)
        allOff()
        GPIO.output(10, True) # Tree no 8 Blue
        time.sleep(chaseTime)
        allOff()
        GPIO.output(25, True) # Tree no 5 Blue
        time.sleep(chaseTime)
        allOff()
        GPIO.output(24, True) # Tree no 13 Red
        time.sleep(chaseTime)
        allOff()
        GPIO.output(23, True) # Tree no 23 Green
        time.sleep(chaseTime)
        allOff()
        GPIO.output(16, True) # Tree no 9 Blue
        time.sleep(chaseTime)
        allOff()
        GPIO.output(13, True) # Tree no 3 Red
        time.sleep(chaseTime)
        allOff()
        GPIO.output(20, True) # Tree no 17 Red
        time.sleep(chaseTime)
        allOff()

    if (buttonStatus == 6):
        climbTime = 0.2

        # Up
        allOff()
        GPIO.output(7, True) # Tree no 22 Red
        GPIO.output(10, True) # Tree no 8 Blue
        GPIO.output(23, True) # Tree no 23 Green
        time.sleep(climbTime)

        allOff()
        GPIO.output(6, True) # Tree no 16 Green
        GPIO.output(15, True) # Tree no 2 Green
        GPIO.output(22, True) # Tree no 24 Red
        GPIO.output(20, True) # Tree no 17 Red
        GPIO.output(24, True) # Tree no 13 Red
        GPIO.output(12, True) # Tree no 15 Green
        time.sleep(climbTime)

        allOff()
        GPIO.output(18, True) # Tree no 20 Red
        GPIO.output(4, True) # Tree no 1 Red
        GPIO.output(17, True) # Tree no 10 Green
        GPIO.output(9, True) # Tree no 14 Green
        GPIO.output(13, True) # Tree no 3 Red
        GPIO.output(5, True) # Tree no 7 Red
        GPIO.output(26, True) # Tree no 12 Red
        GPIO.output(8, True) # Tree no 6 Blue
        time.sleep(climbTime)

        allOff()
        GPIO.output(27, True) # Tree no 11 Blue
        GPIO.output(25, True) # Tree no 5 Blue
        GPIO.output(16, True) # Tree no 9 Blue
        GPIO.output(11, True) # Tree no 21 Blue
        time.sleep(climbTime)

        allOff()
        GPIO.output(19, True) # Tree no 18 Red
        GPIO.output(2, True) # Star
        time.sleep(climbTime)

        # Down
        allOff()
        GPIO.output(27, True) # Tree no 11 Blue
        GPIO.output(25, True) # Tree no 5 Blue
        GPIO.output(16, True) # Tree no 9 Blue
        GPIO.output(11, True) # Tree no 21 Blue
        time.sleep(climbTime)

        allOff()
        GPIO.output(18, True) # Tree no 20 Red
        GPIO.output(4, True) # Tree no 1 Red
        GPIO.output(17, True) # Tree no 10 Green
        GPIO.output(9, True) # Tree no 14 Green
        GPIO.output(13, True) # Tree no 3 Red
        GPIO.output(5, True) # Tree no 7 Red
        GPIO.output(26, True) # Tree no 12 Red
        GPIO.output(8, True) # Tree no 6 Blue
        time.sleep(climbTime)

        allOff()
        GPIO.output(6, True) # Tree no 16 Green
        GPIO.output(15, True) # Tree no 2 Green
        GPIO.output(22, True) # Tree no 24 Red
        GPIO.output(20, True) # Tree no 17 Red
        GPIO.output(24, True) # Tree no 13 Red
        GPIO.output(12, True) # Tree no 15 Green
        time.sleep(climbTime)

        allOff()
        GPIO.output(7, True) # Tree no 22 Red
        GPIO.output(10, True) # Tree no 8 Blue
        GPIO.output(23, True) # Tree no 23 Green
        time.sleep(climbTime)
