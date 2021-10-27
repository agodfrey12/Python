import board
import digitalio
import time

led = digitalio.DigitalInOut(board.A7)
led.direction = digitalio.Direction.OUTPUT

##Button Presses
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

while True:
    print(time.monotonic())
    time.sleep(0.1)
    if buttonA.value == True:
        led.value = True
    else:
        led.value = False