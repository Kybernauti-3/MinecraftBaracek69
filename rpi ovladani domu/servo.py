from machine import Pin, PWM
import utime

servo = PWM(Pin(0))

servo.freq(50)

def dvere_otevrit():
    servo.duty_u16(1475)

def dvere_zavrit():
    servo.duty_u16(4100)

while True:
    control = input('''
ovladani dveri: 
[1] otevrit
[2] zavrit

''')

    if(str(control) == "1"):
        dvere_otevrit()
    if(str(control) == "2"):
        dvere_zavrit()
