import RPi.GPIO as GPIO
import dht11

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
SIGNAL_PING=13
SIGNAL_PING2=18
sensor=dht11.DHT11(pin=SIGNAL_PING)
sensor2=dht11.DHT11(pin=SIGNAL_PING2)

resultado=sensor.read()
resultado2=sensor2.read()

if resultado.is_valid():
    temperatura=resultado.temperature
    humedad=resultado.humidity
    print("Temperatura [C]:", temperatura)
    print("Humedad [%]:", humedad)
    
else:
    print("Error")
    
if resultado2.is_valid():
    temperatura2=resultado2.temperature
    humedad2=resultado2.humidity
    print("Temperatura2 [C]:", temperatura2)
    print("Humedad2 [%]:", humedad2)
    
else:
    print("Error2")

GPIO.cleanup()