#from housectrl import dvere_otevrit,dvere_zavrit, door_switch
from machine import Pin
button = Pin(1, Pin.IN, Pin.PULL_DOWN)

import network
from umqtt.simple import MQTTClient

# 147.228.121.4:80

#broker = 'broker.hivemq.com'
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
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect("kokot", "minecraft69")
    print("Pripojuji k WiFi...")
    while not wlan.isconnected():
        pass
    print("Pripojeno k WiFi")
    # Connect to MQTT broker
    client = MQTTClient("pico", "147.228.121.4", 80)
    client.connect()
    print("Pripojeno k MQTT")

    client.publish(topic, b"Pico connected")

    client.subscribe(topic)

    while True:
        client.check_msg()

        #if button.value():
         #   stav = door_switch(stav)

main()