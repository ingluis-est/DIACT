import RPi.GPIO as GPIO
import time
#al definir usamos el valor de la GPIO, por ejemplo si
#si usamos el GPIO11, ponemos Variable(pin al cual esta conectado)=11
GPIO.setwarnings(False)
s2 = 24
s3 = 23
s0 = 12
s1 = 16
led= 7
#signal representa el out del sensor
signal = 25
NUM_CYCLES = 10


def setup():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(signal,GPIO.IN, pull_up_down=GPIO.PUD_UP)
  GPIO.setup(s0,GPIO.OUT)
  GPIO.setup(s1,GPIO.OUT)
  GPIO.setup(s2,GPIO.OUT)
  GPIO.setup(s3,GPIO.OUT)
  GPIO.setup(led,GPIO.OUT)
  
  print('Medicion en proceso')
  GPIO.output(s0,True)
  GPIO.output(s1,True)
  GPIO.output(s2,False)
  GPIO.output(s3,False)
  GPIO.output(led,False)
  print('Inicializando sensor GY-31')
  time.sleep(5)
  print("\n")
  
def loop():
  temp = 1
  GPIO.output(led,True)
  while(1):      
    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.LOW)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start      #seconds to run for loop
    red  = NUM_CYCLES / duration   #in Hz
    #print("red value - ",red)

    GPIO.output(s2,GPIO.LOW)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    blue = NUM_CYCLES / duration
    #print("blue value - ",blue)
    
    GPIO.output(s2,GPIO.HIGH)
    GPIO.output(s3,GPIO.HIGH)
    time.sleep(0.3)
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
      GPIO.wait_for_edge(signal, GPIO.FALLING)
    duration = time.time() - start
    green = NUM_CYCLES / duration
    print("red: {:.2f}, blue: {:.2f}, green: {:.2f}".format(red,blue,green))
    time.sleep(2) 

    color=max(red,blue,green)
    if color==red:
        print('red')
    elif color==blue:
        print('blue')
    else:
        print('green')
      
def endprogram():
    GPIO.cleanup()

if __name__=='__main__':
    
    setup()

    try:
        loop()

    except KeyboardInterrupt:
        endprogram()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      