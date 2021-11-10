import time
import board
import pulseio

# Initialize PWM output for the servo (on pin A2):
servo = pulseio.PWMOut(board.A2, frequency=50)

# Create a function to simplify setting PWM duty cycle for the servo:
def servo_duty_cycle(pulse_ms, frequency=50):
    period_ms = 1.0 / frequency * 1000.0
    duty_cycle = int(pulse_ms / (period_ms / 65535.0))
    return duty_cycle

def angle2pulse(angle):
    return (0.603 + 0.0099 * angle)

# Main loop will run forever moving between 1.0 and 2.0 ms long pulses:
while True:
    angle = angle2pulse(0.0)
    print('Angle =', angle)
    servo.duty_cycle = servo_duty_cycle(angle)
    #pulse_ms = 0.65
    #print('Milli Second Pulse = ',pulse_ms)
    #servo.duty_cycle = servo_duty_cycle(pulse_ms)
    time.sleep(1.0)