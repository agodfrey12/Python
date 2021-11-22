### DOINK code ###

### notes for the future
## make it write to a txt file on board
## use switch to start 
## switch other way to stop


# make sure file is named code.py

import math
import board
import time
import busio
import digitalio
import adafruit_lis3mdl # magnetometer
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33 # accel and rate gyro

#print(dir(adafruit_lis3mdl))
#print(dir(LSM6DS33))

#start time when turned on/reset
start_time = time.monotonic()

#I@C setup
i2c = board.I2C()                           # tells the CPB we are using I2C
sensor1 = LSM6DS33(i2c)                     # sens 1 is the accel/gyro on I2C
sensor2 = adafruit_lis3mdl.LIS3MDL(i2c)     # sens 2 is the magnetometer on I2C

#button presses - make this the switch
buttonA = digitalio.DigitalInOut(board.D4)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

while time.monotonic() - start_time < 40:
    t = time.monotonic() - start_time
    ax,ay,az = sensor1.acceleration         # acceleration data in 3 axis
    wx,wy,wz = sensor1.gyro                 # rate gyro data in 3 axis
    bx,by,bz = sensor2.magnetic             # magnetometer data in 3 axis
    heading = math.atan2(by,bx)*180/math.pi
    print(heading)
    #print(t,ax,ay,az,wx,wy,wz,bx,by,bz)
    time.sleep(0.05)