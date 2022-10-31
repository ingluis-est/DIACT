#!/usr/bin/env python3          
                                
import signal                   
import sys
import RPi.GPIO as GPIO

BUTTON_GPIO =19
#GPIO 19 encoder left
#GPIO 1 encoder Right
a=0
vueltas=0

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_callback(channel):
    global a, vueltas
    if GPIO.input(BUTTON_GPIO):
        a=a+1
        print(a)
        if a==20:
            a=0
            vueltas=vueltas+1
            print("Vuelta #: ",vueltas)
   
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING, 
            callback=button_callback, bouncetime=5)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()     
