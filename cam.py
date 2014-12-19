#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import picamera
import datetime  # new

def getFileName():  # new
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")

sensorPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

cam = picamera.PiCamera()
cam.resolution= (1024,768)

while True:
    time.sleep(0.1)
    prevState = currState
    currState = GPIO.input(sensorPin)
    if currState != prevState:
        newState = "HIGH" if currState else "LOW"
        print "GPIO pin %s is %s" % (sensorPin, newState)
        if currState:
	    filename='web/static/frames/'+time.strftime('%Y%m%d_%H%M%S.jpg');
            cam.capture(filename) # new

