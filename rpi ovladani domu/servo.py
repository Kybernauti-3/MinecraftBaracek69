from machine import Pin, PWM
import utime

servo = PWM(Pin(0))

servo.freq(50)

while True:
    servo.duty_u16(1350)
    utime.sleep(2)

    servo.duty_u16(4100)
    utime.sleep(2)