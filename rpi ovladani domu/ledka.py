from machine import Pin
from utime import sleep

led = Pin(15,Pin.OUT)


while True:
    control = input('''
ovladani svetla: 
[1] led switch
''')

    if(str(control) == "1"):
        led.toggle()