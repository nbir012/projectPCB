#code for turning LEDs on and off at set times.

#import required libraries
import RPi.GPIO as GPIO
import datetime 
import time

#use BCM naming convention
GPIO.setmode(GPIO.BCM)
#stop warnings appearing on screen
GPIO.setwarnings(False)
#set pin number and output
pin = 22
GPIO.setup(pin,GPIO.OUT)

#run a loop where light turns on at 1000h for 12hrs.
while True:
    time = datetime.datetime.now().strftime("%H:%M")
    if time == "10:00":
        GPIO.output(pin,True)
        time.sleep(43200)
        GPIO.output(pin,False)
    time.sleep(0.030)

