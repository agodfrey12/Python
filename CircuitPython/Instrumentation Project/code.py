### DOINK code ###

# make sure file is named code.py

import board
import time
import busio
import adafruit_lis3mdl
from adafruit_lsm6ds.lsm6ds33 import LSM6DS33

#print(dir(adafruit_lis3mdl))
#print(dir(LSM6DS33))

start_time = time.monotonic()

i2c = board.I2C()
sensor1 = LSM6DS33(i2c)
sensor2 = adafruit_lis3mdl.LIS3MDL(i2c)

accel = sensor1.acceleration
gyro = sensor1.gyro
mag_x, mag_y, mag_z = sensor2.magnetic

while time.monotonic() - start_time < 60:
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (accel))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f radians/s" % (gyro))
    print("X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT".format(mag_x, mag_y, mag_z))
    time.sleep(0.05)