import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.IN)
GPIO.setup(8,GPIO.IN)

count_right=0
flag_right=0
while(1):
	if(GPIO.input(7)==1) and (flag_right==0):
		count_right+=1
		flag_right=1
	elif(GPIO.input(7)==0):
		flag_right=0
	print(count_right)

