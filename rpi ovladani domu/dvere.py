from machine import Pin, PWM
import utime

servo = PWM(Pin(0))
servo.freq(50)

stav = 0

button = Pin(1, Pin.IN, Pin.PULL_DOWN)

def dvere_otevrit():
    
    servo.duty_u16(1475)

def dvere_zavrit():
    servo.duty_u16(4100)

def door_switch(stav):
    if(stav == 1):
        dvere_zavrit()
    else:
        dvere_otevrit()
    return not stav


while True:
    if button.value():
        stav = door_switch(stav)
