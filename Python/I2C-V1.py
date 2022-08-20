import sys
import smbus2 as smbus#,smbus2
import time

I2C_SLAVE_ADDRESS=11
I2C_SLAVE2_ADDRESS=12
I2C_SLAVE3_ADDRESS=13

def ConvertStringsToBytes(src):
    converted=[]
    for b in src:
        converted.append(ord(b))
    return converted

def main(args):
    I2Cbus=smbus.SMBus(1)
    with smbus.SMBus(1) as I2Cbus:
        slaveSelect=input("Wich Arduino (1-3): ")
        cmd=input("Enter comand: ")
        
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
        
        BytesToSend=ConvertStringsToBytes(cmd)
        print("Sent"+str(slaveAddress)+"the"+str(cmd)+"command")
        print(BytesToSend)
        I2Cbus.write_i2c_block_data(slaveAddress, 0x00, BytesToSend)
        time.sleep(1)
        
        while True:
            try:
                data=I2Cbus.read_i2c_block_data(slaveAddress, 0x00,3)
                print(data,"cm")
                time.sleep(2)
                
            except:
                print("remote i/o error")
                time.sleep(2)
                
    return 0

if __name__=='__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("el programa was stopped")
        
    input()
    
