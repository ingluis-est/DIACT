import RPi.GPIO as GPIO
import time

#GPIO 10 -S3 
#GPIO 9 – S2 
#GPIO 11 – OUT 
#GPIO 13 – S1 
#GPIO 21 – S0 
#GPIO 26 – LED
#salidas 
S3=10 
S2=9 
S1=13 
S0=21 
LED=26 
#entradas 
OUT=11
NUM_CYCLES=10

GPIO.setmode(GPIO.BCM)

GPIO.setup(S3,GPIO.OUT) 
GPIO.setup(S2,GPIO.OUT) 
GPIO.setup(S1,GPIO.OUT) 
GPIO.setup(S0,GPIO.OUT) 
GPIO.setup(LED,GPIO.OUT) 

GPIO.setup(OUT,GPIO.IN)

print("Medicion en progreso...") 
GPIO.output(S0, True) 
GPIO.output(S1, True) 

GPIO.output(S3, False) 
GPIO.output(S2, False) 

GPIO.output(LED, False) 

print ("Inicializando sensor GY-31") 
time.sleep(5)

def loop():
    temp=1
    while(1):
        
   #LECTURA DE COLOR ROJO     
GPIO.output(S2,False)
GPIO.output(S3,False) 
time.sleep(0.3) 
start = time.time() 
for impulse_count in range(NUM_CYCLES): 
    GPIO.wait_for_edge(OUT,GPIO.FALLING) 
    duration = time.time() - start
    red  = NUM_CYCLES / duration
    
#LECTURA DE COLOR AZUL
 GPIO.output(S2,False) 
GPIO.output(S3,True) 
time.sleep(0.3) 
start = time.time() 
for impulse_count in range(NUM_CYCLES): 
    GPIO.wait_for_edge(OUT,GPIO.FALLING) 
    duration = time.time() - start 
    blue = NUM_CYCLES / duration 

  #LECTURA DEL COLOR VERDE
   PIO.output(S2,True) 
GPIO.output(S3,True) 
time.sleep(0.3) 
start = time.time() 
for impulse_count in range(NUM_CYCLES):
    GPIO.wait_for_edge(OUT, GPIO.FALLING) 
    duration = time.time() - start 
    green = NUM_CYCLES / duration
    
    print("rojo:{},azul:{},verde:{}".format(red,blue,green))
    color=max(red,blue,green)
    
    if color==red:
        print("el color es rojo")
    elif color==blue:
        print("el color azul")
    else:
        print("el color es verde")