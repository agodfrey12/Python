import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    print(time.monotonic())
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.5)
    led.value = True
    time.sleep(0.2)
    led.value = False
    time.sleep(0.4)
    led.value = True
    time.sleep(0.3)
    led.value = False
    time.sleep(0.3)
    led.value = True
    time.sleep(0.4)
    led.value = False
    time.sleep(0.2)
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.1)
