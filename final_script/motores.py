import RPi.GPIO as GPIO          
from time import sleep

in1 =8
in2 = 7
en1 = 25

in3 = 13
in4 = 14
en2 = 24

temp1=1

GPIO.setmode(GPIO.BCM)

GPIO.setup(en1,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)


p=GPIO.PWM(en1,1000)
p.start(30)

q=GPIO.PWM(en2,1000)
q.start(30)

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='w':
        print("Avanza")
        if(temp1==1):
             GPIO.output(in1,GPIO.LOW)
             GPIO.output(in2,GPIO.HIGH)
             GPIO.output(in3,GPIO.HIGH)
             GPIO.output(in4,GPIO.LOW)
             x='z'

    elif x=='s':
        print("Reversa")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        x='z'

    elif x=='f':
        print("Parar")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
     
        x='z'
        
    elif x=='p':
        print("Parar")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.HIGH)
     
        x='z'

    elif x=='a':
        p.start(50)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        x='z'
    elif x=='d':
        q.start(50)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in1,GPIO.HIGH)
        x='z'

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        q.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        q.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        q.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
        print
        print("Programa Terminado por el usuario")
        print
        