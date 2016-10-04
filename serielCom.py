import time
import serial
import os.path
try:
    ser = serial.Serial('/dev/ttyACM0', 115200)
except:
    ser = serial.Serial('/dev/ttyACM1', 115200)

time.sleep(.1)




def speed(spd):
    ser.write('A')
    if spd == 0:
        ser.write('000')
    elif spd<10:
        ser.write('00'+str(spd))
    elif spd <100:
        ser.write('0'+str(spd))   
    else:
        ser.write(str(spd))
        

def steer(ste):
    ser.write('B')
    if ste == 0:
        ser.write('000')
    elif ste<10:
        ser.write('00'+str(ste))   
    elif ste <100:
        ser.write('0'+str(ste))
    else:
        ser.write(str(ste))

def direct(drt):
    ser.write('C')
    ser.write(str(drt))




#steer(10)
        



