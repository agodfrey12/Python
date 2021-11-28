import math
import time
import board
import busio
import digitalio
from adafruit_circuitplayground.bluefruit import cpb
import adafruit_lis3mdl # magnetometer
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33 # accel and rate gyro

if cpb.switch == False:
    file = open('Test.txt','w')
else:
    print('Not opening file for writing')

start_time = time.monotonic()

#I@C setup
i2c = board.I2C()                           # tells the CPB we are using I2C
sensor1 = LSM6DS33(i2c)                     # sens 1 is the accel/gyro on I2C
sensor2 = adafruit_lis3mdl.LIS3MDL(i2c)     # sens 2 is the magnetometer on I2C

while time.monotonic() - start_time < 60:
    cpb.led = True
    t = time.monotonic() - start_time
    ax,ay,az = sensor1.acceleration         # acceleration data in 3 axis
    wx,wy,wz = sensor1.gyro                 # rate gyro data in 3 axis
    bx,by,bz = sensor2.magnetic             # magnetometer data in 3 axis
    print(t,ax,ay,az,wx,wy,wz,bx,by,bz)
    if cpb.switch == False:
        print('Writing Data to Disk')
        output = str(t) + " " + str(ax) + " " + str(ay) + " " + str(az) + " " + str(wx) + " " + str(wy) + " " + str(wz) + " " + str(bx) + " " + str(by) + " " + str(bz) + str('\n')
        file.write(output)
        file.flush()
        cpb.led = False
    else:
        print('Not logging data. Flip the switch and then hit reset')
    time.sleep(0.5) #sleep for so many seconds between measurements