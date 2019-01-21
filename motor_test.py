#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(6,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

GPIO.output(6,GPIO.HIGH)
GPIO.output(12,GPIO.HIGH)

time.sleep(4)

GPIO.cleanup()
