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
        
#        buttonStatus += 1
        buttonStatus = buttonStatus + 1

        if (buttonStatus == 5):
            buttonStatus = 0

#        GPIO.output(2, True) # Star
#        GPIO.output(4, True) # Tree no 1 Red
#        GPIO.output(5, True) # Tree no 7 Red
#        GPIO.output(6, True) # Tree no 16 Green
#        GPIO.output(7, True) # Tree no 22 Red
#        GPIO.output(8, True) # Tree no 6 Blue
#        GPIO.output(9, True) # Tree no 14 Green
#        GPIO.output(10, True) # Tree no 8 Blue
#        GPIO.output(11, True) # Tree no 21 Blue
#        GPIO.output(12, True) # Tree no 15 Green
#        GPIO.output(13, True) # Tree no 3 Red
#        GPIO.output(15, True) # Tree no 2 Green
#        GPIO.output(16, True) # Tree no 9 Blue
#        GPIO.output(17, True) # Tree no 10 Green
#        GPIO.output(18, True) # Tree no 20 Red
#        GPIO.output(19, True) # Tree no 18 Red
#        GPIO.output(20, True) # Tree no 17 Red
#        GPIO.output(22, True) # Tree no 24 Red
#        GPIO.output(23, True) # Tree no 23 Green
#        GPIO.output(24, True) # Tree no 13 Red
#        GPIO.output(25, True) # Tree no 5 Blue
#        GPIO.output(26, True) # Tree no 12 Red
#        GPIO.output(27, True) # Tree no 11 Blue

#GPIO.add_event_detect(14, GPIO.BOTH, callback=buttonStateChanged)
#GPIO.add_event_detect(14, GPIO.RISING, callback=buttonStateChanged,bouncetime=50)
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
#    pass
#    print buttonStatus

    if (buttonStatus == 0):
        allOff()

    if (buttonStatus == 1):
        allOn()

    if (buttonStatus == 2):
        around()

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

#    if (buttonStatus == 5):
#        allOff()
#        #LedPin = 2
#        two = GPIO.PWM(2, 1000)     # set Frequece to 1KHz
#        two.start(0)                     # Duty Cycle = 0
#        four = GPIO.PWM(4, 1000)     # set Frequece to 1KHz
#        four.start(0)                     # Duty Cycle = 0
#        five = GPIO.PWM(5, 1000)     # set Frequece to 1KHz
#        five.start(0)                     # Duty Cycle = 0
#        six = GPIO.PWM(6, 1000)     # set Frequece to 1KHz
#        six.start(0)                     # Duty Cycle = 0
#        seven = GPIO.PWM(6, 1000)     # set Frequece to 1KHz
#        seven.start(0)                     # Duty Cycle = 0
#        while True:
#                for dc in range(0, 101, 4):   # Increase duty cycle: 0~100
#                    two.ChangeDutyCycle(dc)     # Change duty cycle
#                    four.ChangeDutyCycle(dc)     # Change duty cycle
#                    five.ChangeDutyCycle(dc)     # Change duty cycle
#                    six.ChangeDutyCycle(dc)     # Change duty cycle
#                    seven.ChangeDutyCycle(dc)     # Change duty cycle
#                    time.sleep(0.05)
#                time.sleep(1)
#                for dc in range(100, -1, -4): # Decrease duty cycle: 100~0
#                    two.ChangeDutyCycle(dc)
#                    four.ChangeDutyCycle(dc)
#                    five.ChangeDutyCycle(dc)
#                    six.ChangeDutyCycle(dc)
#                    seven.ChangeDutyCycle(dc)
#                    time.sleep(0.05)
#                time.sleep(1)
