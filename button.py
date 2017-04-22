import  RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    inputValue = GPIO.input(17)
    if (inputValue == False):
        print("Button press ")
    time.sleep(0.3)
