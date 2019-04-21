import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN)#rechts
GPIO.setup(16,GPIO.IN)#links

while  True:
    print(str(GPIO.input(20))+" #rechts")
    print(str(GPIO.input(16))+" #links")
    time.sleep(0.5)
