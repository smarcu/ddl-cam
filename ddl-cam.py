import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED PIN
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

# BUTTON PIN
BUTTON_PIN = 17
GPIO.setup(BUTTON_PIN, GPIO.IN,pull_up_down=GPIO.PUD_UP)

def led( state ): 
	print "LED state ", state
	if state == True:
		GPIO.output(LED_PIN, GPIO.HIGH)
	else:
		GPIO.output(LED_PIN, GPIO.LOW)

def takePicture():
	print "Take Picture!"


# monitor button
while True:
    inputValue = GPIO.input(BUTTON_PIN)

    if (inputValue == False):
        print("Button press ")
	led (True)
	takePicture()
	time.sleep(1);
	led (False)

    time.sleep(0.8)
