from machine import Pin
import utime

led = Pin(2, Pin.OUT)

button = Pin(1,Pin.IN)

while True:
    print(button.value())
    if button.value()==1:
        led.toggle()
        utime.sleep(0.2)
