#code for turning LEDs on and off at set times.

#import GPIO library for use of RPi's GPIO pins
import RPi.GPIO as GPIO
#import time library to allow use of time to control off/on
import time
#use BCM naming convention
GPIO.setmode(GPIO.BCM)
#stop warnings appearing on screen
GPIO.setwarnings(False)
#use pin 22 to control LEDs
GPIO.setup(22,GPIO.OUT)
print "LED on"
#use pin 22 to provide 
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print "LED off"
GPIO.output(18,GPIO.LOW)
