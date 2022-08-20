import RPi.GPIO as GPIO
import time

#GPIO 10 -S3 
#GPIO 9 – S2 
#GPIO 11 – OUT 
#GPIO 13 – S1 
#GPIO 21 – S0 
#GPIO 26 – LED
GPIO.setmode(GPIO.BCM)
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

#lectura de color rojo  
GPIO.output(S2,False) 
GPIO.output(S3,False) 
time.sleep(0.3) 
start = time.time() 
for impulse_count in range(NUM_CYCLES): 
    GPIO.wait_for_edge(OUT,GPIO.FALLING) 
    duration = time.time() - start
    red  = NUM_CYCLES / duration    

 
#lectura de color azul 
GPIO.output(S2,False) 
GPIO.output(S3,True) 
time.sleep(0.3) 
start = time.time() 
for impulse_count in range(NUM_CYCLES): 
    GPIO.wait_for_edge(OUT,GPIO.FALLING) 
    duration = time.time() - start 
    blue = NUM_CYCLES / duration 


#lectura de color verde 
GPIO.output(S2,True) 
GPIO.output(S3,True) 
time.sleep(0.3) 
start = time.time() 
for impulse_count in range(NUM_CYCLES):
    GPIO.wait_for_edge(OUT, GPIO.FALLING) 
    duration = time.time() - start 
    green = NUM_CYCLES / duration        