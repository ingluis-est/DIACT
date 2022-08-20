#Libraries
import serial
ser = serial.Serial('GPIO14',9600)
while True:
	read_serial=ser.readline()
	print(read_serial)