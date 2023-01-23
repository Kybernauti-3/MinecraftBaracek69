#from housectrl import dvere_otevrit,dvere_zavrit, door_switch
from machine import Pin
#button = Pin(1, Pin.IN, Pin.PULL_DOWN)
import time
led = Pin("LED", Pin.OUT)
led.value(1)
led.value(0)

import network
from umqtt.simple import MQTTClient

# 147.228.121.4:80


jmenowifi = "xxx,4GHz"
heslowifi = "xxx"

#broker = 'broker.hivemq.com'
broker = "147.228.121.4"
port = 80
topic = "minecraftbaracek"

def on_message(topic, msg):
    print("Received message on topic: {}, with payload: {}".format(topic, msg))
    if msg == "opendoor":
        print("xd")
        #dvere_otevrit()
    elif msg == "closedoor":
        print("lol")
        #dvere_zavrit()


def main():
    # Connect to Wi-Fi
    
    print("Pripojuji k WiFi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(jmenowifi, heslowifi)

    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print('Cekam na pripojeni...')
        time.sleep(1)

    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    else:
        s = 3
        while s > 0:
            s -= 1
            led.value(1)
            time.sleep(0.5)
            led.value(0)
            time.sleep(0.5)
        
        #print('connected')
        status = wlan.ifconfig()
        print( 'Pripojeno k ' + jmenowifi + ' ' + 'IP: ' + status[0] )



    # Connect to MQTT broker
    client = MQTTClient("pico", broker, port)
    client.connect()
    print("Pripojeno k MQTT")

    client.publish(topic, b"Pico connected")

    #client.subscribe(topic)

    #while True:
     #   client.check_msg()

        #if button.value():
         #   stav = door_switch(stav)

main()