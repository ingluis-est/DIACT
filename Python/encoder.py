import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
pin=16

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)
    
while True:
    if GPIO.input(pin)==0:
        cont=0
        cont=cont+1
        print(" ",cont)
        
    else:
        print("alto")
        
        
def endprogram():
    GPIO.cleanup()
