from machine import Pin, PWM
import utime
import random

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


Led_R = PWM(Pin(2))
Led_G = PWM(Pin(3))
Led_B = PWM(Pin(4))
# Define the frequency
Led_R.freq(2000)   
Led_G.freq(2000)   
Led_B.freq(2000)   

while True:
    if button.value():
        stav = door_switch(stav)

        R=random.randint(0,65535)
        G=random.randint(0,65535)
        B=random.randint(0,65535)
        print(R,G,B)
        Led_R.duty_u16(R)
        Led_G.duty_u16(G)
        Led_B.duty_u16(B) 
        utime.sleep_ms(1000)