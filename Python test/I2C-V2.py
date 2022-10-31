import sys
import smbus2 as smbus
import time

I2C_SLAVE_ADDRESS=11
I2C_SLAVE2_ADDRESS=12
I2C_SLAVE3_ADDRESS=13

def main(args):
    I2Cbus=smbus.SMBus(1)
    with smbus.SMBus(1) as I2Cbus:
        slaveSelect=input("Seleccione un arduino esclavo (1-3): ")
        
        if slaveSelect=="1":
            slaveAddress=I2C_SLAVE_ADDRESS
        elif slaveSelect=="2":
            slaveAddress=I2C_SLAVE2_ADDRESS
        elif slaveSelect=="3":
            slaveAddress=I2C_SLAVE3_ADDRESS
        else:
            print(slaveSelect="1")
            print(type(slaveSelect))
            print("no Slave Select")
            quit()

        I2Cbus.write_i2c_block_data(slaveAddress, 0x12, [])
        time.sleep(1)
        
        while True:
            try:
                data=I2Cbus.read_i2c_block_data(slaveAddress, 0x0,3)
                print("Datos del arduino nano actualizada")
                #print(data,"cm") #Decomentar para ver los datos en formato de lista
                print(f'Ultrasonico derecho   --> {data[0]}')
                print(f'Ultrasonico frontal   --> {data[1]}')
                print(f'Ultrasonico izquierdo --> {data[2]}')
                print("="*40)
                
                time.sleep(2)

            except:
                print("Error de conexion I2C")
                time.sleep(2)
                
    return 0

if __name__=='__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("el programa se ha detenido")
        
    input()
    
