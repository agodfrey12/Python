import time
import board
from analogio import AnalogIn

analogin = AnalogIn(board.A3)

def getVoltage(pin):  # helper
    return (pin.value)

bootuptime = time.monotonic()
while True:
    time_elapsed = time.monotonic() - bootuptime
    val = getVoltage(analogin)
    print((time_elapsed,val))
    time.sleep(0.1)