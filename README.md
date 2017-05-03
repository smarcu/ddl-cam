# ddl-cam
# D&amp;D Lab Camera

A simple DIY camera using Raspberry Pi.

##Raspberry Pi Pinout
 * pinout [https://pinout.xyz/](https://pinout.xyz/)
 * in this project using pin GND, BCM 18, BCM 17

## Hardware
###LED connection
 * using pin (GND and BCM 18)
 * GND: [https://pinout.xyz/pinout/ground](https://pinout.xyz/pinout/ground)
 * BCM 18: [https://pinout.xyz/pinout/pin12_gpio18](https://pinout.xyz/pinout/pin12_gpio18)
 * Test pins:

 ```python led.py to test led```

###Button connection
 * using pin (GND and BCM 17)
 * GND: [https://pinout.xyz/pinout/ground](https://pinout.xyz/pinout/ground)
 * BCM 17: [https://pinout.xyz/pinout/pin11_gpio17](https://pinout.xyz/pinout/pin11_gpio17)
- run: python button.py 

## Software
###Take a picture
 * Take a picture into the current folder (resolution 800x600)

 ```raspistill -t 1 -w 800 -h 600 -o {imgName}```

### Full script
 * ddl-cam.py script monitors the button state, takes a picture and turns the led on during shot time.
 * pictures are taken in the same folder where you run the scripts
 * you can copy the files from remote machine using scp
 * example, copy all jpg files from 192.168.1.15 (your current raspberry pi ip)  to your current folder

```scp pi@192.168.1.15:/home/pi/ddl-cam/*.jpg .```