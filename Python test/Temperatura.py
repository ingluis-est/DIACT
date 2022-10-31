import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using GPIO 12, 16
SIGNAL_PING=16
SIGNAL_PING2=12


while True:
    sensor=dht11.DHT11(pin=SIGNAL_PING)
    sensor2=dht11.DHT11(pin=SIGNAL_PING2)
    resultado=sensor.read()
    resultado2=sensor2.read()
    temperatura=resultado.temperature
    humedad=resultado.humidity
    print("Temperatura 1 [C]:", temperatura)
    print("Humedad 1 [%]:", humedad)
    temperatura2=resultado2.temperature
    humedad2=resultado2.humidity
    print("Temperatura 2 [C]:", temperatura2)
    print("Humedad 2 [%]:", humedad2)
    print("="*40)

    time.sleep(3)


GPIO.cleanup()